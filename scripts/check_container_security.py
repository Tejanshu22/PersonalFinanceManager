"""DAY-006 real Docker builds with fake env sentinels; no real credentials read.

Run from a clean review checkout with Docker available. Builds local images only,
never starts services, and removes only sentinels/directories it created.
"""
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import tarfile
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[1]
IMAGE = "personal-finance-local-frontend"
DEV_PACKAGES = {
    "eslint-config-next", "@next/eslint-plugin-next", "fast-glob", "micromatch",
    "braces", "eslint", "typescript", "tsx", "@playwright/test", "playwright",
    "playwright-core", "prettier",
}


def run(*args, capture=False):
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=capture, check=True)
    return result.stdout.strip() if capture else None


def inspect_layers(image, destination, token, runtime=False):
    """Inspect every saved layer, including files hidden by a later deletion.

    Read tar members without extracting them. Never print file contents.
    """
    run("docker", "image", "save", "-o", str(destination), image)
    violations, packages, paths = set(), set(), set()
    layers = 0
    with tarfile.open(destination) as archive:
        manifest = json.load(archive.extractfile("manifest.json"))
        for layer_name in dict.fromkeys(x for item in manifest for x in item["Layers"]):
            layers += 1
            with tarfile.open(fileobj=archive.extractfile(layer_name), mode="r|*") as layer:
                for member in layer:
                    path = PurePosixPath(member.name)
                    if path.name == ".env" or path.name.startswith(".env."):
                        violations.add("environment-file path in image layer")
                    if ".git" in path.parts:
                        violations.add("source-control history in image layer")
                    if runtime and path.parts[:1] == ("app",):
                        paths.add(str(path))
                        if str(path).startswith(("app/frontend/tests/", "app/docs/", "app/config/",
                                                  "app/frontend/app/", "app/frontend/components/",
                                                  "app/frontend/lib/")):
                            violations.add("unneeded source or fixture in runtime")
                    if not member.isfile():
                        continue
                    stream = layer.extractfile(member)
                    if runtime and path.name == "package.json" and "node_modules" in path.parts:
                        content = stream.read()
                        if token in content:
                            violations.add("synthetic sentinel content in layer")
                        try:
                            name = json.loads(content).get("name", "")
                            packages.add(name)
                            if name in DEV_PACKAGES:
                                violations.add("development package in runtime: " + name)
                        except (ValueError, UnicodeError):
                            pass
                        continue
                    tail = b""
                    while chunk := stream.read(1024 * 1024):
                        if token in tail + chunk:
                            violations.add("synthetic sentinel content in layer")
                        tail = chunk[-len(token):]
    if violations:
        raise RuntimeError("; ".join(sorted(violations)))
    if runtime:
        assert "app/frontend/server.js" in paths, "Standalone server missing"
        assert any(p.startswith("app/frontend/.next/static/") for p in paths), "Static assets missing"
    return {"layers_checked": layers, "violations": [], "runtime_packages": sorted(packages)}


def main():
    # A Dockerfile-specific ignore takes precedence; never silently test another policy.
    for name in ["frontend/Dockerfile.dockerignore", "backend/Dockerfile.dockerignore"]:
        if (ROOT / name).exists():
            raise RuntimeError("Review Dockerfile-specific ignore before running: " + name)
    token = ("FINNEST_FAKE_CONTAINER_SENTINEL_" + uuid.uuid4().hex).encode()
    created, directories, preserved = [], [], {}
    report = {"status": "running", "synthetic_only": True}
    output = ROOT / "tmp/day06-container-security.json"
    output.parent.mkdir(exist_ok=True)
    try:
        parents = [ROOT, ROOT / "frontend", ROOT / "backend",
                   ROOT / "frontend/.day06-context-probe/nested",
                   ROOT / "backend/.day06-context-probe/nested"]
        for parent in parents:
            missing = []
            current = parent
            while not current.exists():
                missing.append(current)
                current = current.parent
            for directory in reversed(missing):
                directory.mkdir()
                directories.append(directory)
            for name in [".env", ".env.local", ".env.production", ".env.development", ".env.test"]:
                file = parent / name
                if file.exists():
                    preserved[file] = hashlib.sha256(file.read_bytes()).digest()
                    continue  # Never overwrite founder settings; all such paths must still be excluded.
                with file.open("xb") as stream:
                    stream.write(b"DAY06_FAKE_ONLY=" + token + b"\n")
                created.append(file)
        report["synthetic_paths"] = [str(p.relative_to(ROOT)).replace("\\", "/") for p in created]
        report["existing_env_files_preserved"] = len(preserved)
        # --no-cache-filter forces the context guard even though excluded sentinels
        # intentionally do not affect Docker's COPY cache keys.
        run("docker", "build", "--no-cache-filter", "build", "--target", "build",
            "-f", "frontend/Dockerfile", "-t", IMAGE + "-security-build", ".")
        run("docker", "compose", "build", "frontend", "api")
        with tempfile.TemporaryDirectory(prefix="day06-layers-", dir=ROOT / "tmp") as temporary:
            assert Path(temporary).resolve().is_relative_to((ROOT / "tmp").resolve())
            for label, image in [("build", IMAGE + "-security-build"), ("runtime", IMAGE),
                                 ("backend", "personal-finance-local-api")]:
                report[label] = inspect_layers(image, Path(temporary) / (label + ".tar"),
                                               token, runtime=label == "runtime")
        details = json.loads(run("docker", "image", "inspect", IMAGE, capture=True))[0]
        assert details["Config"]["User"] == "node", "Runtime must run as node"
        assert details["Config"]["Cmd"] == ["node", "frontend/server.js"]
        report["runtime_image_bytes"] = details["Size"]
        report["runtime_user"] = details["Config"]["User"]
        report["status"] = "pass"
    except BaseException:
        report["status"] = "fail"
        raise
    finally:
        # Exact paths only; no recursive deletion or user-file replacement.
        for file in created:
            assert file.resolve().is_relative_to(ROOT)
            file.unlink(missing_ok=True)
        for directory in reversed(directories):
            assert directory.resolve().is_relative_to(ROOT)
            directory.rmdir()
        report["sentinels_removed"] = all(not p.exists() for p in created)
        report["existing_env_files_unchanged"] = all(
            p.exists() and hashlib.sha256(p.read_bytes()).digest() == digest
            for p, digest in preserved.items())
        if not report["existing_env_files_unchanged"]:
            report["status"] = "fail"
        output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print("Container security result:", report["status"], "—", output.relative_to(ROOT))
        assert report["existing_env_files_unchanged"], "Existing environment file changed"


if __name__ == "__main__":
    main()

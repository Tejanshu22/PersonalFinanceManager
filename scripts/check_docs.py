"""Check repository-relative Markdown file targets; no external network requests."""
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    paths = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, text=True
    ).splitlines()
    checked = 0
    errors = []
    for name in paths:
        path = ROOT / name
        if path.suffix.lower() != ".md":
            continue
        content = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8-sig"), flags=re.S)
        for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", content):
            target = raw.strip().split(' "')[0].strip("<>")
            if urlsplit(target).scheme or target.startswith("//"):
                continue
            filename = unquote(target.split("#")[0])
            if not filename:
                continue
            checked += 1
            if not (path.parent / filename).resolve().exists():
                errors.append(f"{name}: missing {target}")
    print(f"Checked {checked} local Markdown file targets; {len(errors)} missing.")
    print("External URLs and heading fragments are not checked.")
    for error in errors:
        print(error)
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())

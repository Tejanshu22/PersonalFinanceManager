# Update an existing PersonalFinanceManager repository safely

The starter ZIP contains root-level project files, not a Git repository and not a nested folder. **Do not force-push** or delete existing work.

## Option A: Existing repo has only a README (or just a few files)

From your local clone, assuming the downloaded ZIP is in the parent directory:

```bash
cd PersonalFinanceManager
unzip -n ../PersonalFinanceManager_Starter_Pack.zip
python scripts/validate_manifest.py
python -m unittest discover -s tests -v
git status
git diff --check
git add .
git commit -m "chore: add FINNest project starter and progress tracker"
git push origin HEAD
```

`unzip -n` preserves existing files, including your edited README. If it skipped old tracking scripts or docs, use Option B to bring those files up to date.

## Option B: Existing repo contains an older version of the starter pack

Use a separate extracted copy so you can inspect changes first:

```bash
mkdir -p ../FINNest-starter-new
unzip -o ../PersonalFinanceManager_Starter_Pack.zip -d ../FINNest-starter-new
# Review which files differ before copying:
diff -qr . ../FINNest-starter-new || true
# Intentionally refresh supplied starter files except your custom README:
rsync -av --exclude='README.md' --exclude='.git/' ../FINNest-starter-new/ ./
git diff --check
git status
python scripts/validate_manifest.py
python -m unittest discover -s tests -v
# Carefully review diffs of any previously customized scripts or docs before committing.
git add .
git commit -m "chore: refresh FINNest tracker for PersonalFinanceManager"
git push origin HEAD
```

`rsync` is normally available on macOS/Linux; on Windows, use Git Bash/WSL or copy the extracted files manually and compare your changes. This refresh can overwrite customized non-README files, so always review `git diff` before committing. No command here deletes files or resets Git history.

## Final checklist

1. Confirm `.github/workflows/ci.yml` and `.github/workflows/sync-progress.yml` are visible on GitHub. Hidden directories can be missed in website uploads.
2. Confirm the repo's default branch is `main` or adjust the workflow branch settings.
3. Enable **Issues** and **Actions**; allow workflow contents write access as appropriate.
4. Run `bash scripts/first_run_github.sh --dry-run`, then `--apply` only when ready to create your initial issues.
5. Run Actions → **Synchronize project progress** manually and verify that `docs/PROGRESS.md` updates.
6. Do not label an issue `verified` until acceptance criteria, tests, and human review are finished.
7. Never commit real financial records, secrets, PAN numbers, or customer identity documents.

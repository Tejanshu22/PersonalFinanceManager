# FINNest — existing repository and setup reference

**Target repo:** https://github.com/Tejanshu22/PersonalFinanceManager

This is an existing repository on **master** with tracking sync commits and generated issue links. The current remote settings and CI state still require verification. Preserve existing history and edits. The archive/import instructions below are a reference for separately authorized setup work, not steps to rerun during DAY-001. Do not upload, commit, push, dispatch workflows or change settings as part of the documentation draft.

## Prerequisites

- Have write access to `Tejanshu22/PersonalFinanceManager`.
- Prefer the repository to be **private** during development. Do not commit any real bank statements, PAN or Aadhaar details, passwords, access tokens, or unredacted financial data.
- Recommended: Git, Python 3.12+, Node 22+, GitHub CLI (`gh`).
- Preserve `master`; both local workflows already target it. Verify remote defaults/protection before any separately authorized setup change.

## Get the files into GitHub

### Option A — GitHub website (no Git CLI)

1. Open https://github.com/Tejanshu22/PersonalFinanceManager and sign in.
2. Extract `PersonalFinanceManager_Starter_Pack.zip` on your computer.
3. In the repository, choose **Add file → Upload files**, then drag the extracted files and folders into the repository root. GitHub's website may not accept hidden `.github` items reliably through drag-and-drop or large folder uploads; verify `.github/workflows/sync-progress.yml` and `.github/workflows/ci.yml` appear after uploading. If files are missing, use the Git method below.
4. When an initial upload is separately authorized, preserve `master` and use the repository's reviewed contribution process. Inspect the repo tree—`README.md`, `AGENTS.md`, `data/`, `tracking/`, `scripts/`, `.github/` and `docs/` should be at the top level.

### Option B — Git / GitHub CLI (recommended)

Run in a terminal from the directory containing the downloaded **root-level** `PersonalFinanceManager_Starter_Pack.zip`:

```bash
gh auth login
gh repo clone Tejanshu22/PersonalFinanceManager
cd PersonalFinanceManager
# Extract the ZIP's contents into THIS directory (repo root), not a nested folder.
unzip -n ../PersonalFinanceManager_Starter_Pack.zip
# Review any differences if the repository had existing files.
git status
git add .
git commit -m "chore: initialize FINNest planning and verified-progress tracker"
git push origin HEAD
```

If the ZIP lives in another path, change the `unzip` path accordingly. `unzip -n` avoids overwriting existing files. If Git says there is nothing to commit, check whether the expected files are already present. If `gh repo clone` or `git push` fails, authenticate with an account that has repo access.

## Configure GitHub tracking

1. In repository settings, enable **Issues** and **Actions**.
2. In **Settings → Actions → General → Workflow permissions**, enable read/write permissions if allowed; the `sync-progress.yml` workflow explicitly declares `contents: write, issues: read`.
3. For an initial small batch of issues, use:

```bash
bash scripts/first_run_github.sh --dry-run
bash scripts/first_run_github.sh --apply
```

The first command prints what would happen. The second creates exact tracking labels and up to twelve initial Issues (`FIN-###`, `DAY-###`). GitHub CLI authentication is required. If the branch is protected against bot writes, progress sync's auto-commit step must be changed to an approved PR workflow or a permitted bot exception.

4. Run **Actions → Synchronize project progress → Run workflow** (or use `gh workflow run sync-progress.yml -R Tejanshu22/PersonalFinanceManager`).
5. Confirm a new sync commit appears when there are status changes. Verify `tracking/Project_Checklist.xlsx` and `docs/PROGRESS.md` were regenerated.
6. Require merged PR, passing CI, human acceptance, relevant professional reviews and updated docs before authorized verification/closure. Issue #1 needs explicit owner approval. Test status transitions with synthetic local tests; do not close/reopen real project issues merely to test checkmarks. See [verification details](GITHUB_AUTOMATION.md).

## Independent local check

```bash
python scripts/validate_manifest.py
python -m unittest discover -s tests -v
```

> WARNING: `python scripts/sync_progress.py --no-github` intentionally resets generated statuses to `Planned`. Only run for fresh/local demonstrations, not after GitHub Issues are active.

## What is automatic and what is not

**Automatic after setup:** GitHub Issue status → generated Markdown progress, CSV feature/day checklist, XLSX tracker, completion log, release statuses. A manual workflow run is also available for troubleshooting. It does not run on a time schedule.

**Not automatic:** Implementing code, approving tests, deciding tax/regulatory correctness, architecture prose, or public release. Astra should update human-maintained code/architecture/security docs with reviewed changes, and only human reviewers should apply the `verified` label.

## Start Day 1

Open [DAY_01_KICKOFF.md](DAY_01_KICKOFF.md) and use existing [Issue #1](https://github.com/Tejanshu22/PersonalFinanceManager/issues/1) for DAY-001. The documentation draft awaits review; do not create a duplicate issue or mark the day finished.

## Push carefully into an existing repository

An imported starter archive is not a substitute for this repository's Git history. Do **not** use `git push --force` or delete previous work. Pushes require separate authorization.

- The recommended command `unzip -n` skips existing files, including your edited README; compare skipped files manually if you need the latest version.
- Run `git status` and `git diff --check` before committing.
- Ensure the hidden `.github/workflows/` directory was uploaded; GitHub Actions will not start without it.
- If GitHub displays a workflow-permissions error, inspect **Settings → Actions → General** and `master` protection. Propose an approved pull-request workflow if needed; do not weaken protection or modify working configuration automatically.
- Workbook updates happen in GitHub after Actions runs; downloaded `.xlsx` copies on your laptop do not sync automatically.

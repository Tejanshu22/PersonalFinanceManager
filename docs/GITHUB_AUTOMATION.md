# FINNest — GitHub auto-checklist and documentation setup

## What updates automatically?

When a GitHub Issue is opened, labeled, closed, reopened, edited or unlabelled, **GitHub Actions** downloads issue statuses and regenerates:

- `tracking/Feature_Checklist.csv` — Excel-/Google-Sheets-friendly feature tracker (194 rows).
- `tracking/Daily_Checklist.csv` — 85-day tasks with automated checkmarks.
- `tracking/Project_Checklist.xlsx` — Excel workbook with Overview, Features, Daily Plan.
- `docs/PROGRESS.md` — verified totals by release, blocked and needs-review items.
- `docs/COMPLETION_LOG.md` — timestamped index of verified and closed items with issue links.
- `docs/FEATURE_CATALOG.md` — status and acceptance criteria for every feature.
- `docs/ROADMAP.md` — day-by-day roadmap with verified state.
- `tracking/status.json` — machine-readable statistics.

`docs/ARCHITECTURE.md`, `docs/SECURITY.md`, `docs/TAX_POLICY.md`, etc. require **actual code change review**; the bot does not fabricate architecture descriptions from commits. Astra should edit those when changes are made.

## Setup when repository exists

1. Use the existing repository [Tejanshu22/PersonalFinanceManager](https://github.com/Tejanshu22/PersonalFinanceManager). We cannot confirm its present visibility from here; **make it private** while credentials, tax/security plans and financial test materials are being developed. Commit the root contents of the starter pack (not a nested `FINNest_Starter_Repo` directory).
2. Set its default branch to `main`. Enable GitHub Actions. Go to repository Settings → Actions → General and allow workflows to have read/write permissions if your policy permits. The workflow itself declares `contents: write, issues: read`.
3. If you protect `main` against bot pushes, either make a controlled exception for the action or change the workflow's final commit step to create a review PR; **auto-commit will not succeed against a protected main without permission**. For a serious finance project, the PR route may be preferable.
4. Under Issues → Labels, create `in-progress`, `blocked`, `verified` (and optionally `canceled`) exactly in lowercase. Or run `bash scripts/first_run_github.sh --apply` after installing/authenticating GitHub CLI. These label names drive status rules.
5. Create Issue titles beginning with the stable IDs, e.g. `[FIN-011] Normalize dates` or `[DAY-016] Deduplication`. See `.github/ISSUE_TEMPLATE/` for forms. To avoid typing everything, **preview** issue creation with `python scripts/bootstrap_issues.py --kind both --limit 12`; then set `GITHUB_REPOSITORY=Tejanshu22/PersonalFinanceManager` and `GITHUB_TOKEN` (or `GH_TOKEN`) with issue write access, and run the command with `--apply`. It skips existing task IDs. Create only the next ~10–20 items at first; you do not need all 279 issues (194 feature items plus 85 daily tasks) on day one.
6. Run Actions → **Synchronize project progress** → **Run workflow**. First sync correctly shows 0 verified items. Then create/close a test issue with label `verified` and re-run to confirm a checkmark appears.
7. A development PR references a specific feature Issue and can close it using GitHub's normal issue reference. After tests and acceptance are independently checked, apply `verified`. The workflow updates the workbook and Markdown automatically.

## Status semantics

| GitHub Issue state | Tracker status | Checked? |
|---|---|---|
| Missing or open, no progress label | Planned | ☐ |
| Open + `in-progress` | In Progress | ☐ |
| Open + `blocked` | Blocked | ☐ |
| Closed, no `verified` | Needs Review | ☐ |
| Closed + `verified` | Verified Done | ☑ |
| Reopened after verified | Planned / In Progress | ☐ |
| Canceled/wontfix | Blocked | ☐ |

Only closed-and-verified is done. A PR being merged does **not** automatically grant verified status. This deliberate human approval gate matters for tax, finance and security-sensitive work.

## Local testing (no GitHub access needed)

```bash
python scripts/validate_manifest.py
python -m unittest discover -s tests -v
python scripts/sync_progress.py --no-github
npm install --prefix tools/tracker --no-audit --no-fund --ignore-scripts
node tools/tracker/build_xlsx.js
```

**Important:** `--no-github` resets generated progress to all Planned; do not commit those results after you have linked real GitHub issues. To sync real issues locally, set `GITHUB_REPOSITORY=Tejanshu22/PersonalFinanceManager` and `GITHUB_TOKEN` with read access to issues and run `python scripts/sync_progress.py`.

## Limitations & security

- Workflow will **not** actually sync to GitHub until you create a repository and enable it. These files are ready-to-install scaffolding.
- Repository default branch must be `main` or you must update the workflow branch names.
- GitHub Actions permissions and organization policies may prevent auto-commit; inspect failed workflow logs, do not claim success until a test run commits.
- Auto-generated documents reflect **issue statuses** and curated manifest data, not verified claims from arbitrary commits. Meaningful product/code docs still need developer updates.
- Never paste live financial statements, PAN, identity docs, access tokens or private user information into issues/PRs, CI artifacts or prompts.
- The workbook generator uses an npm dependency in standard GitHub runners; security-scan and lock/pin dependencies for production use.
- The current implementation is for a single-repository V1. For multiple repos/large teams, migrate to GitHub Projects API only after the need is clear.

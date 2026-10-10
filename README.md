# FINNest — Personal finance & tax-readiness app (working name)

**Repository:** https://github.com/Tejanshu22/PersonalFinanceManager  
**Display brand:** FINNest (temporary; configurable)  
**First-time GitHub setup:** [docs/START_HERE_GITHUB.md](docs/START_HERE_GITHUB.md)  
**Updating an existing repository:** [docs/UPDATE_EXISTING_REPO.md](docs/UPDATE_EXISTING_REPO.md)  
**Day 1 kickoff:** [docs/DAY_01_KICKOFF.md](docs/DAY_01_KICKOFF.md)

> **Status: planning / starter pack. No product code or real GitHub sync has been deployed.**

**Mission:** Help Indian professionals organize uploaded financial statements, understand cash flow, prepare tax documents, and securely share limited information with a CA. AI explains calculations; it does not invent financial figures.

## Start here

1. Read [the product requirements](docs/REQUIREMENTS.md) and [the complete feature catalog](docs/FEATURE_CATALOG.md).
2. Review the [85-day schedule](docs/ROADMAP.md), [current progress](docs/PROGRESS.md), and [tracked CSVs](tracking/). A [verification log](docs/COMPLETION_LOG.md) records reviewed completions.
3. Follow [GitHub automation setup](docs/GITHUB_AUTOMATION.md) to enable issue-based syncing.
4. Review the [commercial plan](docs/MONETIZATION.md) and [planned screens](docs/SCREENS.md). Follow [security](docs/SECURITY.md), [tax review](docs/TAX_POLICY.md), and [release gates](docs/RELEASE_CHECKLIST.md) before collecting real data.
5. Use [AGENTS.md](AGENTS.md) as the repository instructions for Astra.

## Source of truth

| Source | Role |
|---|---|
| `data/features.json` | Stable feature IDs, release, acceptance and scope |
| `data/daily_plan.json` | Stable DAY-001 through DAY-085 tasks |
| GitHub Issues | Progress status and review gate (when connected) |
| `config/brand.json` | Display name, tagline and configurable branding |
| `tracking/Feature_Checklist.csv` | Auto-generated Excel-friendly checklist |
| `tracking/Daily_Checklist.csv` | Auto-generated 85-day daily checklist |
| `tracking/Project_Checklist.xlsx` | Auto-generated multi-sheet Excel tracker |
| `docs/PROGRESS.md` / `COMPLETION_LOG.md` / `FEATURE_CATALOG.md` / `ROADMAP.md` | Generated project status documents |

### Verification rule

A checkbox becomes checked (`☑`) only when its corresponding GitHub Issue **is closed** **and has the `verified` label**. Closing without verification displays **Needs Review**. Labels like `in-progress` and `blocked` update status immediately. Never use issue closure or an AI-generated PR alone as proof of completeness.

## Local usage (before GitHub connection)

```bash
python scripts/sync_progress.py --no-github
python -m unittest discover -s tests -v
```

When connected, GitHub Actions regenerates Markdown, CSV, JSON and XLSX and commits the new tracked files. Run `python scripts/bootstrap_issues.py --kind both --limit 12` to preview initial GitHub Issues; add `--apply` and repository credentials to create them. See [setup guide](docs/GITHUB_AUTOMATION.md).

## Rebranding

Working name is configurable. Brand clearance is **not** complete: do trademark, domain, app store and market checks before public branding.

```bash
python scripts/rebrand.py "YourNewName" --tagline "Your new message"
```

This changes display branding, not immutable feature IDs, database IDs, identity or routes. Files like `Project_Checklist.xlsx` intentionally keep neutral paths across rebrands. Before launch, also verify domains, trademark, app-store presence, legal-entity name and any new mobile bundle IDs.

## V1 exclusions

**No:** automatic tax filing, AA banking feed, scraping bank/tax credentials, investment advice, GST filing, lending, payments transfer, stock trading or full CA practice management. These are later-phase ideas needing additional regulatory and commercial evaluation.

**Private repo recommended:** keep real bank/tax documents OUT of Git, GitHub Issues, PRs, workflow logs and fixtures; use only synthesized or irreversibly redacted test data.

## Existing repository precautions

This starter package contains root-level files (including hidden `.github/`) and no Git history.
Use `unzip -n` when copying into a repository with existing work. Review `git status` before any commit; do **not** force-push.
The workbook in this repository is an initial snapshot; future updates require enabling the GitHub Actions sync workflow.

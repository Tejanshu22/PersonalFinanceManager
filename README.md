# FINNest — Personal finance & tax-readiness app (working name)

**Repository:** https://github.com/Tejanshu22/PersonalFinanceManager  
**Display brand:** FINNest (temporary; configurable)  
**First-time GitHub setup:** [docs/START_HERE_GITHUB.md](docs/START_HERE_GITHUB.md)  
**Updating an existing repository:** [docs/UPDATE_EXISTING_REPO.md](docs/UPDATE_EXISTING_REPO.md)  
**Day 1 kickoff:** [docs/DAY_01_KICKOFF.md](docs/DAY_01_KICKOFF.md)

> **Status: planning foundation; no application implementation.** Local history and generated issue links show tracking sync activity. Live GitHub status still requires verification. The [DAY-001 draft](docs/DAY_01_KICKOFF.md) awaits owner acceptance.

**Mission:** Help Indian professionals organize uploaded financial statements, understand cash flow, prepare tax documents, and securely share limited information with a CA. AI explains calculations; it does not invent financial figures.

## Start here

1. Read [the product requirements](docs/REQUIREMENTS.md) and [the complete feature catalog](docs/FEATURE_CATALOG.md).
2. Review the [85-day schedule](docs/ROADMAP.md), [current progress](docs/PROGRESS.md), and [tracked CSVs](tracking/). A [verification log](docs/COMPLETION_LOG.md) records reviewed completions.
3. Review [GitHub automation](docs/GITHUB_AUTOMATION.md) for the existing `master` workflow and human verification requirements.
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

## Safe local validation

```bash
python scripts/validate_manifest.py
python -m unittest discover -s tests -v
git diff --check
```

GitHub Actions is configured to regenerate Markdown, CSV, JSON and XLSX and commit tracked outputs on `master`. Do not run `sync_progress.py --no-github` against this connected tracker: it resets statuses to Planned. Issue creation, workflow dispatch and pushes require separate authorization. See [tracking guide](docs/GITHUB_AUTOMATION.md).

The approved Day 1 scope defers FIN-027, FIN-063, FIN-066 and FIN-067 to V1.5. The reconciled manifest and regenerated catalog now contain 140 V1 and 14 V1.5 items (194 total). Generated progress preserves the existing cached issue snapshot; this is not a fresh GitHub status sync. See the [reconciliation record](docs/DAY_01_KICKOFF.md). Targets are Day 60 internal functional beta, Day 75 security-reviewed release candidate, Days 76–80 gated real-user beta and Day 85 public launch. These are conditional planning targets; [requirements](docs/REQUIREMENTS.md) and [decisions](docs/DECISIONS.md) describe the distinction from the unchanged roadmap.

## Rebranding

Working name is configurable. Brand clearance is **not** complete: do trademark, domain, app store and market checks before public branding.

```bash
python scripts/rebrand.py "YourNewName" --tagline "Your new message"
```

This changes display branding, not immutable feature IDs, database IDs, identity or routes. Files like `Project_Checklist.xlsx` intentionally keep neutral paths across rebrands. Before launch, also verify domains, trademark, app-store presence, legal-entity name and any new mobile bundle IDs.

## V1 exclusions

**No:** automatic tax filing, AA banking feed, scraping bank/tax credentials, personalized investment recommendations, GST filing, lending, insurance distribution, payments transfer, stock trading or full CA practice management. These are later-phase ideas needing additional regulatory and commercial evaluation.

**Private repo recommended:** keep real bank/tax documents OUT of Git, GitHub Issues, PRs, workflow logs and fixtures; use only synthesized or irreversibly redacted test data.

## Existing repository precautions

This is an existing Git repository on `master`, with root-level files including hidden `.github/`. Preserve history and user edits. If importing an older starter archive, compare files first; `unzip -n` skips existing files but does not establish that new files are appropriate. Review `git status` before any commit; do **not** force-push.
The workbook is a generated snapshot, not a live local spreadsheet connection. The sync workflow owns updates; do not edit it by hand. No real customer financial documents may be collected before the required safeguards in [SECURITY](docs/SECURITY.md) are implemented and verified.

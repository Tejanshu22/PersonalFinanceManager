# FINNest — GitHub tracking and verification workflow

**DAY-001 documentation review · 2026-10-10.** Working scripts and Actions configuration are unchanged.

## Sources and generated outputs

[features.json](../data/features.json) owns stable feature IDs, release, acceptance and scope; [daily_plan.json](../data/daily_plan.json) owns DAY-001 through DAY-085. GitHub issue titles must begin with the corresponding FIN/DAY ID. The tracker rejects duplicate mappings. Missing issues remain Planned.

The [sync workflow](../.github/workflows/sync-progress.yml) responds to issue events, manual dispatch and selected source-file pushes to **master**. It generates [feature CSV](../tracking/Feature_Checklist.csv), [daily CSV](../tracking/Daily_Checklist.csv), [Excel workbook](../tracking/Project_Checklist.xlsx), [progress](PROGRESS.md), [completion log](COMPLETION_LOG.md), [catalog](FEATURE_CATALOG.md), [roadmap](ROADMAP.md) and [status JSON](../tracking/status.json). It commits only its listed generated artifacts to master; it does not approve product work.

Human-owned requirements, architecture, security, tax policy and decision documents need reviewed edits. Do not manually modify generated output or percentages. The Day 1 140-item V1 proposal is intentionally not yet reconciled into the 144-item V1 manifest.

## Existing repository and branch

Preserve PersonalFinanceManager and **master**. Both local Actions files already use master. Local history and generated issue links show sync activity; live GitHub issue/CI/protection state could not be verified during inspection because reads failed with network/TLS errors.

When separately authorized to configure GitHub, inspect existing settings before changing anything. Sync declares contents-write and issues-read permissions; repository rules may still block bot commits. Prefer an approved PR-based approach if protection requires it, rather than weakening protection as an automatic workaround. No configuration or GitHub mutation is part of DAY-001.

Use existing issues where mapped: DAY-001 → #1, FIN-001–008 → #2–9, DAY-002–004 → #10–12 in the inspected local snapshot. Not every one of the 279 work items needs an issue immediately. Never renumber stable IDs to match GitHub numbers.

Bootstrap preview is read-only by default:

```bash
python scripts/bootstrap_issues.py --kind both --limit 12
```

Applying bootstrap, creating labels, dispatching workflows and pushing changes are separate authorized actions. Do not use a real catalog issue as a fake verified completion to test the tracker; synthetic tests cover the status transition without changing project progress.

## Current computed status versus intended workflow

| Current issue state/labels | Current tracker result |
| --- | --- |
| Missing or open, no progress label | Planned |
| Open + in-progress | In Progress |
| Open + blocked | Blocked |
| Closed, no verified | Needs Review |
| Closed + verified, not canceled/wontfix | Verified Done |
| Reopened with verified only | Planned; no completion check |
| canceled or wontfix | Blocked |

The intended workflow also needs **Needs Review for submitted work while its issue stays open**. That mapping is not implemented. Adding a needs-review label alone currently does not change the result. Do not close an unfinished issue simply to obtain this display state. If blocked and in-progress coexist, current code favors Blocked; canceled/wontfix override completion. Other precedence decisions need explicit tests.

## Human verification and required evidence

Generated code, commits, PR merge and issue closure alone never establish Verified Done. Current code checks issue state/labels; it does **not** independently validate CI, PR merge, reviewer identity or evidence. The verified label must be treated as a controlled human attestation.

Before verification, the issue must reference:

1. FIN/DAY scope and acceptance criteria, reviewed implementation or documentation artifact.
2. Merged PR and passing required CI for the relevant revision.
3. Actual test/fixture results and unresolved limitations, not predicted outcomes.
4. Human-reviewed acceptance and financial/security/privacy/tax review where applicable.
5. Updated impacted technical documents and explicit reviewer approval.

Use a PR title/body referencing DAY-001 or FIN-### and link the issue. Keep incomplete work open; avoid automatic closing references until the full gate is satisfied. Only an authorized human may approve applying verified and closing. **Issue #1 requires the owner's explicit approval; this draft does not authorize either action.**

The completion log records issue state and closure time, not the actual time/evidence of independent verification. A green percentage is not launch authorization.

## Safe local checks

```bash
python scripts/validate_manifest.py
python -m unittest discover -s tests -v
git diff --check
```

The tests generate output inside temporary directories; they must not overwrite tracked artifacts. On Windows, filesystem permissions may require an approved execution context for the temporary-directory test. UTF-8 mode may be needed for Unicode fixtures.

Do not run sync_progress.py with --no-github on the connected working tracker: it intentionally resets generated status to Planned. Isolated demonstrations may use it only outside tracked outputs. Real sync reads GitHub state and writes artifacts; it is not a read-only inspection command. Workbook generation also writes tracked output and is unnecessary for this documentation pass.

## Recorded engineering follow-ups

See T-01–T-07 in [DECISIONS](DECISIONS.md). They require separate implementation approval:

- Represent open submitted work as Needs Review and test status precedence.
- Validate manifests and issue mappings before generation/commit; current CI validates manifests separately, but sync itself does not run that validation gate.
- Guard one-time build_manifest.py and build_daily_plan.py against overwriting authored content.
- Preserve master compatibility and verify remote protection/permissions.
- Preserve IDs and generated ownership; improve evidence expectations and regression coverage.
- Review workbook dependency locking/pinning and testing without unnecessary installations.

Never put raw financial records, PAN, account identifiers, secrets or sensitive prompts in issues, PRs or workflow logs. Current CI tests the tracker only; product lint/type/security/financial checks must be added with the application foundation.
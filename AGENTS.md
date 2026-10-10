# FINNest — engineering instructions for Astra

You are contributing to a **real financial-data product**, not a mockup. Observe the repository docs and assigned GitHub issue ID before changing code.

## Required workflow for every feature

1. Read `docs/REQUIREMENTS.md`, `docs/SECURITY.md`, `docs/TAX_POLICY.md`, the feature acceptance criterion in `data/features.json`, and the existing code.
2. Reply with a short implementation plan, relevant files, tests and known risks.
3. Keep changes inside the issue scope, including migrations, APIs, UI and tests.
4. Run tests, lint/type checks and financial fixture validations; attach test output summary to PR.
5. Update **human-owned technical docs** when architecture, APIs, data flow or security assumptions change. Do not manually modify `docs/PROGRESS.md`, `docs/FEATURE_CATALOG.md`, `docs/ROADMAP.md`, or tracked generated sheets; the sync workflow owns them.
6. Reference `FIN-###` or `DAY-###` in PR title/body and link the GitHub issue; closing is not enough to mark completed.
7. Request reviewer acceptance; only after acceptance/CI/security checks are satisfied should the issue be marked `verified` and closed.

## Non-negotiable correctness rules

- Use `Decimal` / exact numeric DB types for money; **never floats for financial totals**.
- Keep investments, own-account transfers, card repayments, refunds and consumption separate.
- Do not modify raw transaction source values; preserve provenance and corrections.
- Never silently accept unreconciled imports; surface partial-data warnings.
- Financial computation is deterministic and covered by golden fixtures.
- Tax rules are effective-date and reporting-year specific, source-linked, human reviewed, versioned and rollback-capable.
- AI only sees approved minimal structured inputs; never give arbitrary SQL or full document DB access.
- No personalized stock/mutual fund purchase/sale advice without legal authorization.
- No direct banking, tax portal or OTP/password scraping.
- Document permissions default to deny; prevent cross-account access in every API.
- No raw bank PDFs, PAN, account identifiers, OAuth tokens, prompts containing sensitive PII, or secrets in Git, log files, test fixtures or PR bodies.
- Use migrations, background job retries and idempotent payment webhook processing.
- Do not rewrite unrelated modules to 'clean up' the project unless approved.
- Use neutral internal IDs; UI branding comes from `config/brand.json` or a consuming application config generated from it.

## Completion gate

`Verified Done` requires: merged PR, passing CI, financial/security/privacy review as applicable, human-reviewed acceptance criteria, updated impacted docs and a GitHub Issue that is **closed with the `verified` label**. If issue closed without that label, automation reports Needs Review.

If requirements conflict or law/tax interpretation is unclear, raise a blocker; do not invent a rule to satisfy tests.

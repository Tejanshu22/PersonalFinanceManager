# FINNest — product requirements and release boundary

**DAY-001 review draft · 2026-10-10 · [Issue #1](https://github.com/Tejanshu22/PersonalFinanceManager/issues/1).** Requirements below are not implemented or verified. The owner approved the scope amendments and milestone definitions; this document and its proposed acceptance thresholds still require review. See [decisions](DECISIONS.md).

## Product and paying customer

Help Indian salaried individuals organize uploaded financial records, understand explainable figures, prepare tax documents and share selected information with their CA. The primary prospective paying customer is the individual managing multiple bank/card records, not the CA practice. Supplementary freelance income organization is included; business bookkeeping and tax calculation are not.

The complete value journey is **Upload → Reconcile → Correct → Understand → Prepare Tax Documents → Share with CA → Upgrade**. Upgrade follows demonstrated value and informed pricing; users retain control of their own data. FINNest remains a working display brand from [brand configuration](../config/brand.json); PersonalFinanceManager remains the repository name and internal IDs stay neutral.

## Personas: hypotheses to validate

No customer interviews or willingness-to-pay evidence have been collected in this repository. Ages and behaviors below describe intended recruitment, not observed market facts.

| Dimension | Primary: salaried professional | Secondary: salary plus other income | Future B2B: CA or small practice |
| --- | --- | --- | --- |
| Profile | Approximately 23–40, Indian salaried individual, bank accounts, cards, investments and tax documents | Salaried individual with supplementary freelance receipts or multiple income sources; personal organization only | CA or small firm coordinating multiple clients and tax preparation |
| Pain hypotheses | Fragmented statements, inflated spending from repayments/transfers, forgotten charges, annual document collection | Mixed income narrations, unclear business/personal boundaries, missing payment or tax evidence | Incomplete client packages, repeated requests, inconsistent period labels, uncontrolled document sharing |
| Current-workaround hypotheses | Bank apps, spreadsheets, email folders, manual notes and CA messages | Spreadsheets, invoices, bank searches and CA consultation | Email, messaging, cloud folders, spreadsheets and existing practice software |
| Reason to try | Trustworthy source-linked monthly picture and less tax-document searching | Separate income sources, correct records and present unresolved questions to a CA | Receive an organized, scoped package with coverage and unresolved issues |
| Upload objections | Breach risk, hidden data use, AI exposure, uncertain deletion, startup longevity | Commercial/client information in narrations; fear that estimates are mistaken for tax advice | Client confidentiality, authorization, incorrect summaries and retention obligations |
| Most valuable features | Reconciled imports, corrections, real spending, recurring candidates, monthly report and tax package | Income tagging, provenance, missing-document checklist and CA export | V1 recipient viewer/export; later client requests, roles and multi-client workflow |
| Payment hypothesis | Plus at ₹999/year if recurring clarity exceeds upload effort; seasonal Tax Pack at ₹499 | May value Plus and Tax Pack; no demonstrated higher willingness to pay | Future subscription only if workflow time savings and trust are demonstrated; no price chosen |
| Usage hypothesis | Monthly after statements, occasional charge review, seasonal tax preparation | Monthly or more often when reconciling receipts; seasonal CA preparation | Seasonal and repeated during active client work; future weekly/daily use unvalidated |

Validate actual past behavior, upload refusal conditions, comprehension and price tradeoffs through the [Day 2 interview plan](DAY_01_KICKOFF.md). Dedicated freelancers, businesses, nonresident/complex cross-border tax cases and full CA practice management are outside the initial product promise.

## Release disposition of every catalog feature

The [manifest](../data/features.json) and [generated catalog](FEATURE_CATALOG.md) still contain **144 V1, 10 V1.5, 20 V2, 8 V3+ and 12 Future items**. The approved four deferrals produce a **proposed 140 V1 / 14 V1.5 split**, pending separately approved manifest reconciliation. No feature is deleted or renumbered.

| IDs | Documentation disposition |
| --- | --- |
| FIN-001–026, FIN-028–062, FIN-064–065, FIN-068–144 | Retain V1; bounded by this document |
| FIN-027 | Defer second bank PDF adapter to V1.5; prioritize first-format reliability |
| FIN-063 | Defer recurring price-increase alerts to V1.5; needs reliable matching/history |
| FIN-066 | Defer financial-health components to V1.5; avoid interpretive scoring in initial release |
| FIN-067 | Defer upload reminders/monthly notifications to V1.5; monthly report itself remains V1 |
| FIN-145–154 | Retain V1.5: additional formats, goals, manual assets/liabilities, net worth, household view, notifications, classifier improvements and localization |
| FIN-155–174 | Retain V2: professionally validated tax computation and full CA workspace |
| FIN-175–182 | Future regulated integrations; preserve existing V3+ manifest classification |
| FIN-183–194 | Retain Future: broader family/business workflows, professional services, mobile and other expansions |

### V1 required capabilities

1. Verified-email onboarding, session recovery/revocation, owned financial accounts, income types, reporting preferences and honest empty states.
2. CSV with supported mappings, **one thoroughly tested Indian bank PDF format and one card format**. Provider/version selection is pending suitable synthetic or irreversibly anonymized fixtures. Digital-format support must be explicit. Scanned PDFs have no V1 OCR promise: reject safely with an actually supported alternative. Never imply arbitrary PDFs are supported.
3. Preview, normalization, asynchronous status, reconciliation, duplicate/overlap review, classification confidence, manual corrections, undo and source history. Passwords for encrypted PDFs are ephemeral.
4. Source-linked income, consumption, investment and cash-flow views; filters, comparable-period trends, data coverage and monthly reports. No overall financial-health score.
5. Explainable recurring-payment candidates and tentative duplicate/unusual-charge candidates. These are not fraud determinations or cancellation services.
6. Ask My Money using a small documented allowlist of spending, income, recurring and period-comparison queries. Numerical answers come from deterministic tools; unsupported or insufficient-data questions receive explicit limitations.
7. Private Form 16/AIS/TIS and related-document handling, reviewable Form 16 metadata, declared-income document checklists, missing-document reasons and limited reviewed policy information. No tax liability or filing guarantee.
8. Annual CA-ready package, explicit selected-resource sharing, recipient-bound invitation, expiry, revocation and user-visible access history. No firm or multi-client workspace.
9. Free/paid entitlements, hosted checkout, verified payment events, usage limits, receipts and defined cancellation/refund behavior. Tier boundaries remain hypotheses in [monetization](MONETIZATION.md).
10. Security, privacy, support, accessibility, monitoring, backups, recovery, deployment rollback and independent release review. These are release requirements, not optional enhancements.

### Explicit exclusions

No direct Account Aggregator synchronization, bank/tax login or OTP scraping, ITR submission, GST filing, personalized stock/mutual-fund purchase or sale recommendations, lending/origination, insurance distribution, money transfer, trading, broker integration, or other regulated capability in V1. No investment valuation/returns engine, advanced tax calculation, full bookkeeping, native mobile app or full CA SaaS. Later entries are evaluation candidates, not commitments or evidence of legal authorization.

## Financial accuracy contract (proposed for review)

All money uses decimal arithmetic and exact database numeric types. Preserve currency, source amount/text/date, statement/page/row reference, parser version, reconciliation results and correction history. Never overwrite raw source values. V1 initially reports INR only; unsupported currencies must be surfaced without conversion or mixed-currency totals. Decimal precision, rounding mode and boundary behavior must be approved and fixture-tested before implementation; no hidden tolerance may make a mismatch disappear.

| Concept | Required treatment |
| --- | --- |
| Income | Recognized salary, freelance and other income receipts; exclude own transfers, card repayments, refunds, borrowings and investment-principal returns. This is observed receipt income, not taxable income or gross salary. Uncertain credits stay unclassified. |
| Consumption spending | Recognized purchases/services, fees and interest, less matched refunds/reversals under the period rule below; excludes investment contributions, transfers and debt principal. Show unresolved debits separately. |
| Investments | Contributions tracked separately from consumption. Withdrawals/redemptions are not automatically income or gains; no inferred capital-gains calculation. |
| Internal transfers | Link confirmed own-account legs. Exclude from income/consumption; cancel within a consolidated cash-account boundary only when both accounts are included. Show unmatched candidates and transfers crossing a selected-account boundary. |
| Credit-card purchases | Recognize consumption when posted, unless classified as investment/transfer/other. Card statements represent liability activity, not cash-account inflows/outflows. |
| Credit-card repayments | Settlement of liability; not a second expense or income. Bank cash-flow includes the cash outflow; card settlement is not added again to cash flow. Missing purchase history must be disclosed. |
| Refunds | Preserve receipt date and link to original purchase where justified. Proposed default: reduce consumption in the refund posting period, with cross-period annotation; do not silently rewrite an earlier report. Unmatched refunds remain visible for review, not ordinary income. |
| Reversals | Keep both source entries and their relationship; neutralize the confirmed reversed activity without deleting evidence. Cross-period reversals use the same explicit posting-period treatment. |
| Cash flow | Sum posted inflows minus outflows for the selected cash/bank accounts and period. Includes investment cash movements, refunds, financing and card settlement; excludes card purchase rows. Explain transfers crossing the selected boundary. It is not income minus consumption. |
| Savings | Display only a qualified **observed income less net consumption** measure. Show investment contributions separately; do not call this bank balance, available cash, wealth or actual total savings. With material unknown activity or missing coverage, label provisional or withhold the measure. |

Use posted dates for default reporting; preserve transaction/value dates where supplied and expose the chosen basis. Date-only statement values must not shift day through timezone conversion. Same-day identical amounts are not sufficient proof of duplication. Re-import identity and overlap logic must preserve legitimate repeated purchases; matching uncertain transfers/refunds requires review and must not erase rows.

Reconcile cash-account opening balance + credits − debits to closing balance when present, and use a separately specified card liability equation for card statements. Missing balances mean **reconciliation unavailable**, not successful reconciliation. Document exact format-specific equations and any justified source rounding before enabling the adapter.

Coverage is per account and period. Display missing periods/pages, row errors, unsupported accounts, unmatched activity, import freshness and reconciliation state beside totals and in exports/AI results. A user may acknowledge a warning; that does not convert partial data into verified data. Comparable trends require comparable coverage. With no data, show no-data states rather than fabricated zero activity. Reports must record input snapshot, calculation version and correction version so historical output can be reproduced.

## Measurable acceptance matrix

These are **proposed release thresholds, not test results**. Every journey is unimplemented/unverified. “100%” below means the declared, versioned test corpus, not universal real-world accuracy. Each evidence bundle must identify commit/build, fixtures and expected outputs, actual results, defects and human reviewer. Missing evidence fails the gate. Financial expected outputs require independent calculation/review, not copying implementation output.

| Journey / feature IDs | Acceptance and practical threshold | Test and required evidence | Dependencies |
| --- | --- | --- | --- |
| 1. Registration · FIN-009–016 | Valid signup, email verification, login, logout and recovery work; expired/reused tokens and revoked sessions rejected in every security case | Browser/API flow record; token lifecycle and abuse tests; no identity leakage in errors | Auth provider choice, email, session policy, consent notice |
| 2. Supported import · FIN-017–026, 028–031, 033–034 | Every advertised format/version passes the approved corpus; preview precedes finalization; unsupported/scanned/oversized/unsafe files produce actionable failure; job retries do not duplicate imports | Support matrix, safe fixture provenance, parser/queue E2E output including wrong password and partial failure | Private uploads, scanning, isolated workers, selected fixtures |
| 3. Extraction/reconciliation · FIN-018–020, 032, 035, 047, 131 | 100% expected rows, dates, decimal amounts and source references on golden fixtures; exact supported balance checks; every injected omission/mismatch flagged; no silent partial success | Independent expected ledger and balance equations; missing-page, overlap and retry results | Canonical schema, precision policy, parser versions |
| 4. Classification/correction · FIN-036–046 | All rules/edge-case fixtures pass; uncertain rows enter review; user correction and undo preserve raw data and recalculate affected outputs | Versioned rules, confidence meaning, precision/error report on held-out examples; correction/audit E2E | Ledger, reviewed taxonomy and matching policy; numeric confidence calibration pending |
| 5. Income/expense/cash flow · FIN-048–058, 064 | Every golden aggregate matches exactly; no transfer or repayment double count; filters/drill-downs agree; partial coverage stays visible | Salary, investment, refund, reversal, two-account/card and missing-leg fixtures; independent totals | Financial contract approval, ledger and coverage metadata |
| 6. Monthly report · FIN-065 | Every reported number traces to the same snapshot; recalculation is reproducible; corrected/new reports are versioned; incomplete months carry warnings | Monthly boundary and cross-period refund fixtures; report/API/export parity evidence | Analytics, snapshot/versioning, disclosure copy |
| 7. Recurring detection · FIN-059–062 | Candidates show evidence and uncertainty; dismissals persist. Proposed evaluation: ≥90% precision and ≥80% recall on ≥50 independently labeled sequences with ≥20 recurring and ≥20 nonrecurring; sample support and errors reported | Held-out labeled sequences including variable dates/amounts and insufficient history; separate unusual/duplicate-alert case review | Sufficient history, merchant normalization; thresholds need owner approval |
| 8. Ask My Money · FIN-068–076 | Every numerical claim matches authorized tool output and source references; zero unauthorized disclosures/tool calls on adversarial corpus; ≥95% correct answer or justified clarification on ≥50 reviewed questions, plus ≥20 adversarial cases | Versioned prompts/tools/model, exact numeric checks, reviewer rubric; ambiguity, missing-data, injection and quota results | Approved analytics APIs, data minimization, provider review, usage limits |
| 9. Tax documents · FIN-077–080 | Owner-only uploads/tags; reviewable extracted metadata with source locations; corrections never overwrite the source; unsupported extraction does not fabricate fields | Vault access matrix, synthetic Form 16/AIS/TIS fixtures, unsafe-file tests | Upload security, year model, limited extraction support matrix |
| 10. Tax readiness · FIN-081–089 | Every approved scenario produces expected checklist/reasons; unknown income types marked unresolved; 100% published policy items have source, applicability, version and qualified approval | CA-reviewed scenario table; unpublished-rule denial and rollback results; no “ready to file” inference | Declared income types, documents, appointed tax reviewer |
| 11. CA sharing · FIN-090–096 | Only selected snapshot resources available to intended recipient; scope/expiry/revocation checked on every new fetch; all unauthorized cases denied; downloads limitation disclosed | Two-owner/two-recipient negative tests, invite replay, cached-link/revocation tests and audit evidence | Scoped identity, authorization gateway, consent and expiry policy |
| 12. Payments · FIN-097–107 | Paid rights granted only after verified server-side payment; invalid signatures/replays/duplicates/out-of-order events cannot overgrant; agreed expiry/refund/cancellation states pass | Sandbox event/state matrix, entitlement tests, receipt checks; limited production payment/refund evidence before public launch | Gateway/merchant approval, tier and refund decisions, secrets, event storage |
| 13. Security/privacy · FIN-108–126 | All access/consent/export/deletion cases pass; zero cross-owner exposure in reviewed corpus; backup deletion/restore behavior evidenced; no unresolved critical/high security findings | Threat model, independent assessment, processor/retention review, sanitized audit samples, restore and deletion drills | Security/legal reviewers, lifecycle policy, operational ownership |
| 14. Production readiness · FIN-127–144 | All advertised journeys and release gates pass; rollback/restore rehearsed. Proposed budgets: dashboard API p95 ≤2s at 20 concurrent users; supported 100-page imports p95 ≤120s at five concurrent jobs; recovery ≤24h data loss and ≤4h restore | Declared staging dataset/hardware/workload, load report and recovery timing; accessibility/core mobile checks, go/no-go record | Budget approval, infrastructure, monitoring/support, independent reviews and controlled beta |

Performance and corpus minimums are planning proposals requiring review against format limits, costs and reviewer capacity. Passing small synthetic corpora does not establish production accuracy. Publish limitations and use controlled beta evidence to reassess claims; do not lower a safety gate to meet a date.

Business outcomes use defined denominators in [monetization](MONETIZATION.md). There is no validated activation, conversion, retention or revenue target yet.
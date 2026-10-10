# FINNest — 85-day plan

> AUTO-GENERATED. Edit `data/daily_plan.json` to change the planned work.

**Assumption:** 6–8 focused hours/day, five working days/week. This is a planning estimate, not a release guarantee.

## Week 1 — Research and requirements

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 1 | Freeze V1 scope, personas and measurable success criteria | Planned | [GitHub](https://github.com/Tejanshu22/PersonalFinanceManager/issues/1) |
| ☐ | 2 | Interview five salaried prospective users and summarize buying pain | Planned | [GitHub](https://github.com/Tejanshu22/PersonalFinanceManager/issues/10) |
| ☐ | 3 | Interview five more prospects and two CAs; identify reviewer | Planned | [GitHub](https://github.com/Tejanshu22/PersonalFinanceManager/issues/11) |
| ☐ | 4 | Analyze competitors, pricing, compliance risks and name conflicts | Planned | [GitHub](https://github.com/Tejanshu22/PersonalFinanceManager/issues/12) |
| ☐ | 5 | Create user journeys, wireframes, landing page and waitlist | Planned | — |


## Week 2 — Architecture and secure foundations

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 6 | Scaffold Next.js, FastAPI, PostgreSQL, CI and local staging | Planned | — |
| ☐ | 7 | Design canonical ledger, ownership, Decimal amounts and migrations | Planned | — |
| ☐ | 8 | Implement secure authentication and session recovery | Planned | — |
| ☐ | 9 | Build private file uploads, scanning and async job infrastructure | Planned | — |
| ☐ | 10 | Implement audit events, monitoring, environment isolation and threat model | Planned | — |


## Week 3 — First CSV importer

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 11 | Canonical transaction/account/source data contract | Planned | — |
| ☐ | 12 | CSV upload with flexible column matching | Planned | — |
| ☐ | 13 | Normalize dates, amounts and narration safely | Planned | — |
| ☐ | 14 | Async import workflow with row-level error recovery | Planned | — |
| ☐ | 15 | Import preview and user approve/reject experience | Planned | — |


## Week 4 — Categorization and correctness

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 16 | Deduplication and idempotent transaction imports | Planned | — |
| ☐ | 17 | Merchant normalization and classification rules | Planned | — |
| ☐ | 18 | Own-account transfer, refunds, reversals and card payment logic | Planned | — |
| ☐ | 19 | Corrections, edit history, scoped user-defined rules | Planned | — |
| ☐ | 20 | Golden fixtures and accounting edge-case tests | Planned | — |


## Week 5 — PDF and card statements

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 21 | PDF framework, parser isolation, file limits and ephemeral passwords | Planned | — |
| ☐ | 22 | Bank-specific PDF parser #1 with tests | Planned | — |
| ☐ | 23 | Format variants and regression tests for first bank parser | Planned | — |
| ☐ | 24 | Credit-card statement adapter with purchase/payment/refund logic | Planned | — |
| ☐ | 25 | Extraction preview and reconciliation warnings | Planned | — |


## Week 6 — Data pipeline hardening

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 26 | Bank-specific PDF parser #2 | Planned | — |
| ☐ | 27 | Unsupported-format handling and manual fallback UX | Planned | — |
| ☐ | 28 | Overlapping statement periods and reconciliation rules | Planned | — |
| ☐ | 29 | Job retry, failure analytics and duplicate protection | Planned | — |
| ☐ | 30 | Alpha test on anonymized fixtures; fix blocking parser bugs | Planned | — |


## Week 7 — Financial dashboard

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 31 | Specify and implement income, spending and investment metrics | Planned | — |
| ☐ | 32 | Category/merchant trends and reliable aggregation APIs | Planned | — |
| ☐ | 33 | Build responsive dashboard with live imported data | Planned | — |
| ☐ | 34 | Last-import timestamps, partial coverage labels and drill-down | Planned | — |
| ☐ | 35 | Validate totals against independent calculations | Planned | — |


## Week 8 — Recurring intelligence

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 36 | Recurring-charge detection heuristics | Planned | — |
| ☐ | 37 | Subscription and commitments dashboard | Planned | — |
| ☐ | 38 | Duplicate and unusual-spend alert candidates | Planned | — |
| ☐ | 39 | Monthly report builder with supporting details | Planned | — |
| ☐ | 40 | Health metric components with coverage restrictions | Planned | — |


## Week 9 — AI money assistant

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 41 | Allowlisted AI financial tool interface with no arbitrary SQL | Planned | — |
| ☐ | 42 | Question routing and deterministic tool results | Planned | — |
| ☐ | 43 | AI chat UI and usage limits | Planned | — |
| ☐ | 44 | Source-backed answers, prompt redaction and traceability | Planned | — |
| ☐ | 45 | Adversarial and numeric test corpus including prompt injection | Planned | — |


## Week 10 — Tax-document foundation

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 46 | Private tax vault and document metadata | Planned | — |
| ☐ | 47 | Historic FY/AY plus new Tax Year data model | Planned | — |
| ☐ | 48 | Form 16 upload and reviewed fields | Planned | — |
| ☐ | 49 | AIS/TIS upload workflow and document tagging | Planned | — |
| ☐ | 50 | Income-specific tax-readiness and missing-document checks | Planned | — |


## Week 11 — Policy and expert review

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 51 | Versioned tax-rule metadata with source/effective date | Planned | — |
| ☐ | 52 | Policy admin entry, review and publish workflow | Planned | — |
| ☐ | 53 | Historic source linking and rule-set applicability | Planned | — |
| ☐ | 54 | Audit, rollback and protected publication process | Planned | — |
| ☐ | 55 | Qualified tax-expert check of supported content and examples | Planned | — |


## Week 12 — CA collaboration

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 56 | Generate accountant-ready annual financial package | Planned | — |
| ☐ | 57 | Explicit limited-scope consent for CA sharing | Planned | — |
| ☐ | 58 | Time-limited invitation and scoped CA access | Planned | — |
| ☐ | 59 | Revocation, expiry and access audit tests | Planned | — |
| ☐ | 60 | End-to-end beta integration test and feature freeze | Planned | — |


## Week 13 — Billing

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 61 | Plan and entitlements model with backend-enforced limits | Planned | — |
| ☐ | 62 | Payment checkout and paid-order verification | Planned | — |
| ☐ | 63 | Webhook signature checks, replay and idempotency tests | Planned | — |
| ☐ | 64 | Refunds, failed payments, receipts and cancellations | Planned | — |
| ☐ | 65 | Pricing/upgrade/paywall UX and sandbox billing rehearsal | Planned | — |


## Week 14 — Legal and operational hardening

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 66 | Consent and privacy controls in app | Planned | — |
| ☐ | 67 | User data exports, deletion requests and retention policies | Planned | — |
| ☐ | 68 | Legal review of privacy, terms, cancellation and disclaimers | Planned | — |
| ☐ | 69 | Support workflow and incident escalation | Planned | — |
| ☐ | 70 | Automated security checks and remediation list | Planned | — |


## Week 15 — Release candidate

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 71 | Full integration/E2E regression and authorization tests | Planned | — |
| ☐ | 72 | Financial correctness and all supported format fixtures | Planned | — |
| ☐ | 73 | Concurrency/performance and robustness tests | Planned | — |
| ☐ | 74 | Restore backups and incident recovery rehearsal | Planned | — |
| ☐ | 75 | Independent security assessment and fix gating | Planned | — |


## Week 16 — Controlled paid beta

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 76 | Invite limited consenting users after release gate | Planned | — |
| ☐ | 77 | Assess import quality, corrections and user comprehension | Planned | — |
| ☐ | 78 | Test real early payments and refunds in controlled rollout | Planned | — |
| ☐ | 79 | Interview paid/free beta testers and solve biggest problems | Planned | — |
| ☐ | 80 | Document support, onboarding and production rollout | Planned | — |


## Week 17 — Public launch

| Done | Day | Task | Status | Issue |
| --- | --- | --- | --- | --- |
| ☐ | 81 | Fix high-priority testing and feedback findings | Planned | — |
| ☐ | 82 | Final end-to-end, auth, tax-policy and billing regression | Planned | — |
| ☐ | 83 | Verify production alerts, recovery and rollback | Planned | — |
| ☐ | 84 | Full release rehearsal and go/no-go decision | Planned | — |
| ☐ | 85 | Limited public launch if all security and accuracy gates pass | Planned | — |


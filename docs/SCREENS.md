# FINNest — planned application screen inventory

These are proposed V1 user flows, **not implemented screens**. Keep the product web-first and accessible on mobile browsers.

DAY-001 review: screen scope follows [requirements](REQUIREMENTS.md). FIN-027, FIN-063, FIN-066 and FIN-067 are now V1.5 in the reconciled feature manifest and generated catalog. Daily-roadmap adjustments remain separate proposals in [decisions](DECISIONS.md).

| Screen | What users can do | Notes |
| --- | --- | --- |
| Landing page | Understand promise, limits, pricing, early access | Must avoid misleading financial/CA claims |
| Register / login | Create, verify, access, recover account | Managed authentication and audit controls |
| Privacy & preferences | Manage use purposes, AI consent, reporting period/timezone and withdrawal | No consent dark patterns; reminder preferences deferred with FIN-067 |
| Financial account manager | Add bank/card account metadata | Never collect bank-login credentials |
| Upload center | Upload supported CSV, one bank and one card PDF format; inspect support matrix | Providers pending safe fixtures; scanned/unsupported files fail gracefully |
| Import processing status | See queued, processing, complete/partial/error | Retry/fallback |
| Transaction preview | Review extracted rows and reconciliation warnings | Do not silently accept uncertain totals |
| Transaction list | Filter, search, correct, undo, inspect source | Precision and provenance |
| Money dashboard | Income, consumption spending, investments, cross-account cash flow | Explicit freshness/coverage labels |
| Spending analytics | Category/merchant trends and source drilldown | Transfer/refund treatment correct |
| Recurring costs | Review subscription/commitment candidates | Candidate not certainty |
| Unusual activity | See anomalies and acknowledge/dismiss | Not fraud detection guarantees |
| Monthly report | See what changed and why | Exportable with source data |
| Ask My Money | Ask grounded financial questions | Allowlisted queries and citations to transactions |
| Tax vault | Upload Form 16, AIS/TIS, related documents | User/private permissions |
| Tax readiness | View relevant missing documents/issues by tax period | Not a complete tax assessment |
| Tax-policy library | Read published reviewed tax changes and sources | No unapproved rule used in calculations |
| CA package | Prepare and download summary and unresolved questions | Sources and assumptions disclosed |
| CA invitation | Share selected records with time limit, revoke future access | Scope-specific consent/audit; downloaded copies cannot be recalled |
| Billing | Plan, payment, receipts, cancellation/refund | Server-side entitlement rules |
| Settings & security | Devices/sessions, export/delete, access history | Account owner only |
| Help / support | Report import errors safely | Never default-upload raw user documents to tickets |
| Administrative policy review | Review, approve and publish tax-rule metadata | Limited staff-only privileges |
| Administrative support | Inspect non-sensitive operational state | Least-privilege staff access |

## Later screens

- Financial-health components (FIN-066) and upload/monthly reminder preferences (FIN-067), V1.5.
- Additional bank adapter support (FIN-027) and recurring price-increase insights (FIN-063), V1.5.
- Tax regime and liability simulator (after independently validated engine).
- Full CA practice dashboard and client workflow.
- Net worth, assets and liabilities; financial goals; family view.
- Regulated data connections and authorized e-filing.
- Native Android/iOS when retention justifies the expense.

# FINNest — planned application screen inventory

These are proposed V1 user flows, **not implemented screens**. Keep the product web-first and accessible on mobile browsers.

| Screen | What users can do | Notes |
| --- | --- | --- |
| Landing page | Understand promise, limits, pricing, early access | Must avoid misleading financial/CA claims |
| Register / login | Create, verify, access, recover account | Managed authentication and audit controls |
| Privacy & preferences | Manage use purposes, reporting period/timezone, notifications | No consent dark patterns |
| Financial account manager | Add bank/card account metadata | Never collect bank-login credentials |
| Upload center | Upload CSV, supported PDFs and view supported formats | Scanning, size checks, private storage |
| Import processing status | See queued, processing, complete/partial/error | Retry/fallback |
| Transaction preview | Review extracted rows and reconciliation warnings | Do not silently accept uncertain totals |
| Transaction list | Filter, search, correct, undo, inspect source | Precision and provenance |
| Money dashboard | Income, consumption spending, investments, cross-account cash flow | Explicit freshness/coverage labels |
| Spending analytics | Category/merchant trends and source drilldown | Transfer/refund treatment correct |
| Recurring costs | Review subscription/commitment candidates | Candidate not certainty |
| Unusual activity | See anomalies and acknowledge/dismiss | Not fraud detection guarantees |
| Monthly report | See what changed and why | Exportable with source data |
| Financial health | Transparent calculated components | Overall score not shown with insufficient data |
| Ask My Money | Ask grounded financial questions | Allowlisted queries and citations to transactions |
| Tax vault | Upload Form 16, AIS/TIS, related documents | User/private permissions |
| Tax readiness | View relevant missing documents/issues by tax period | Not a complete tax assessment |
| Tax-policy library | Read published reviewed tax changes and sources | No unapproved rule used in calculations |
| CA package | Prepare and download summary and unresolved questions | Sources and assumptions disclosed |
| CA invitation | Share selected records with time limit, revoke access | Scope-specific consent and audit |
| Billing | Plan, payment, receipts, cancellation/refund | Server-side entitlement rules |
| Settings & security | Devices/sessions, export/delete, access history | Account owner only |
| Help / support | Report import errors safely | Never default-upload raw user documents to tickets |
| Administrative policy review | Review, approve and publish tax-rule metadata | Limited staff-only privileges |
| Administrative support | Inspect non-sensitive operational state | Least-privilege staff access |

## Later screens

- Tax regime and liability simulator (after independently validated engine).
- Full CA practice dashboard and client workflow.
- Net worth, assets and liabilities; financial goals; family view.
- Regulated data connections and authorized e-filing.
- Native Android/iOS when retention justifies the expense.

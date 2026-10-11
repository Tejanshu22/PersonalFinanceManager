# FINNest — Feature catalog

> AUTO-GENERATED; edit `data/features.json` instead of editing this document.

**Catalog:** 194 atomic features across V1, V1.5, V2, V3+ and Future.

## V1 — Discovery & product

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-001 | Define persona and measurable problem | Planned | Signed-off V1 product brief with exclusions and success metrics |
| ☐ | FIN-002 | Customer discovery interviews | Planned | At least 10 interviews summarized with evidence and insights |
| ☐ | FIN-003 | CA workflow discovery | Planned | At least two professional workflow interviews documented |
| ☐ | FIN-004 | Competitor and pricing research | Planned | Comparison and tested price hypotheses recorded |
| ☑ | FIN-005 | Brand configuration and rename policy | Verified Done | Display name comes only from config and rebrand guide exists |
| ☐ | FIN-006 | Landing page and waitlist | Planned | Privacy-conscious waitlist and signup flow works |
| ☐ | FIN-007 | Product acceptance criteria | Planned | V1 functions have explicit pass/fail conditions |
| ☐ | FIN-008 | Risk register and decision log | Planned | Major assumptions and risks have owners and follow-ups |


## V1 — Identity & onboarding

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-009 | Secure sign-up and login | Planned | Signup, login and logout tested end to end |
| ☐ | FIN-010 | Verified email onboarding | Planned | User email verification works |
| ☐ | FIN-011 | Password reset and session revocation | Planned | Reset and revoked sessions cannot access accounts |
| ☐ | FIN-012 | Financial account profile | Planned | User can create and manage owned bank/card account metadata |
| ☐ | FIN-013 | Income-type onboarding | Planned | Salary, freelance, investment and other income types selected |
| ☐ | FIN-014 | Preferences and reporting timezone | Planned | Reporting window and timezone persisted correctly |
| ☐ | FIN-015 | Sensitive session management | Planned | Expired/revoked sessions are rejected server-side |
| ☐ | FIN-016 | Onboarding tutorial and empty states | Planned | No-data users see correct next steps, not fake numbers |


## V1 — Import & document ingestion

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-017 | CSV import with column mapping | Planned | Supported CSV imports with preview and schema checks |
| ☐ | FIN-018 | Money amount and debit-credit normalization | Planned | Negative/positive and debit/credit variants normalized |
| ☐ | FIN-019 | Date parsing and timezone semantics | Planned | Dates parsed consistently with stated date assumptions |
| ☐ | FIN-020 | Canonical statement model | Planned | Each import preserves source, period and ownership |
| ☐ | FIN-021 | Import queue and progress indicator | Planned | Async jobs show pending, success, partial failure and error |
| ☐ | FIN-022 | File type/size limits | Planned | Unsupported or oversized files rejected safely |
| ☐ | FIN-023 | Secure upload and temporary download URLs | Planned | Unauthorized users cannot read uploaded files |
| ☐ | FIN-024 | Password-protected PDFs handled safely | Planned | Password is ephemeral and never logged or stored |
| ☐ | FIN-025 | PDF parser framework | Planned | Bank-specific parser adapters run in isolated workflow |
| ☐ | FIN-026 | Supported bank PDF parser #1 | Planned | Confirmed fixture suite passes |
| ☐ | FIN-028 | Supported card statement parser #1 | Planned | Credit-card purchases, repayments, fees and refunds classified |
| ☐ | FIN-029 | Manual import preview and confirmation | Planned | Imported rows not persisted as final without validation path |
| ☐ | FIN-030 | Unsupported format guidance | Planned | Clear fallbacks and support request available |
| ☐ | FIN-031 | Partial extraction warnings | Planned | Missing pages/rows are surfaced explicitly |
| ☐ | FIN-032 | Statement reconciliation | Planned | Where balances exist, integrity checks flag discrepancies |
| ☐ | FIN-033 | Re-import and overlap handling | Planned | Re-import does not double-count rows |
| ☐ | FIN-034 | Raw source traceability | Planned | Every transaction links to source statement reference |


## V1.5 — Import & document ingestion

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-027 | Supported bank PDF parser #2 | Planned | Confirmed fixture suite passes |


## V1 — Transaction data quality

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-035 | Normalized transaction ledger | Planned | Decimal amount, account and source metadata stored |
| ☐ | FIN-036 | Deterministic merchant recognition | Planned | Merchant rules identify common narrations |
| ☐ | FIN-037 | Rules-first categorization engine | Planned | Transparent category decisions for known patterns |
| ☐ | FIN-038 | User transaction editing | Planned | Manual edits persist and show audit history |
| ☐ | FIN-039 | User-defined category rules | Planned | Repeated merchant fixes become scoped rules |
| ☐ | FIN-040 | Internal transfer candidate matching | Planned | Own-account transfers are not counted as income/spend |
| ☐ | FIN-041 | Refund and reversal detection | Planned | Refunds reverse appropriate spending without fake income |
| ☐ | FIN-042 | Credit-card repayment treatment | Planned | Bank-to-card repayments don't inflate spending |
| ☐ | FIN-043 | Duplicate row identification | Planned | Same rows are ignored on overlapping uploads |
| ☐ | FIN-044 | Uncertain classification queue | Planned | Low-confidence classifications require user review |
| ☐ | FIN-045 | Transaction classification provenance | Planned | Original text and reason/confidence retained |
| ☐ | FIN-046 | Transaction correction undo | Planned | User can reverse a mistaken category edit |
| ☐ | FIN-047 | Source totals mismatch handling | Planned | Reports show unreconciled data warnings |


## V1 — Financial calculations & dashboard

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-048 | Income and actual spending rules | Planned | Salary, refund, investments and transfer separation validated |
| ☐ | FIN-049 | Month-by-month cash flow | Planned | Correct monthly inflows/outflows shown by account/period |
| ☐ | FIN-050 | Investment-contribution metric | Planned | Investments tracked separately from consumption spending |
| ☐ | FIN-051 | Category breakdowns | Planned | Charts match canonical transactions |
| ☐ | FIN-052 | Merchant breakdowns | Planned | Merchant totals trace back to rows |
| ☐ | FIN-053 | Cross-account summary | Planned | Combined view excludes internal transfer double count |
| ☐ | FIN-054 | Time-period and account filters | Planned | All analytics respect selected filters |
| ☐ | FIN-055 | Historical comparison | Planned | Period-on-period comparison uses comparable coverage |
| ☐ | FIN-056 | Data coverage/freshness warnings | Planned | Last import and missing statement periods shown |
| ☐ | FIN-057 | Transaction drill-down | Planned | Every aggregate opens supporting transactions |
| ☐ | FIN-058 | Empty/partial-data behavior | Planned | Insufficient data does not generate false precision |


## V1 — Personal finance insights

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-059 | Recurring-charge detector | Planned | Repeated merchant-period sequences produce candidates |
| ☐ | FIN-060 | Subscriptions and fixed commitments view | Planned | Recurring monthly/annual values displayed |
| ☐ | FIN-061 | Potential duplicate payment alerts | Planned | Suspected duplicate charges are clearly labeled as tentative |
| ☐ | FIN-062 | Unusual spending alerts | Planned | Outliers are flagged without fraud accusations |
| ☐ | FIN-064 | Explainable savings metrics | Planned | Cash available and invested cash explicitly distinguished |
| ☐ | FIN-065 | Monthly financial summary report | Planned | Monthly report produced from audited calculations |


## V1.5 — Personal finance insights

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-063 | Recurring price-increase alerts | Planned | Meaningful increase compared with prior payments detected |
| ☐ | FIN-066 | Coverage-aware health components | Planned | Components show evidence and avoid fake overall score |
| ☐ | FIN-067 | Upload reminder and monthly notification preferences | Planned | User controls reminder frequency and channel |


## V1 — Ask My Money AI

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-068 | Approved financial query tools | Planned | Model cannot access DB except via allowlisted functions |
| ☐ | FIN-069 | Safe question-to-tool routing | Planned | Spending, income and comparison intents map correctly |
| ☐ | FIN-070 | Financial chat interface | Planned | Users can ask questions with usable failure messages |
| ☐ | FIN-071 | Source-backed numerical answers | Planned | Every number is derived from backend and traceable |
| ☐ | FIN-072 | Privacy-minimized model prompts | Planned | PAN/account numbers and unrelated financial rows withheld |
| ☐ | FIN-073 | Prompt injection resilience | Planned | Untrusted statement texts cannot override system behavior |
| ☐ | FIN-074 | Ambiguity and missing data responses | Planned | AI acknowledges incomplete account coverage |
| ☐ | FIN-075 | AI usage limits and cost controls | Planned | Server enforces quotas and protects expensive endpoints |
| ☐ | FIN-076 | AI evaluation set | Planned | Numerical, redaction and adversarial tests pass |


## V1 — Tax readiness and policy

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-077 | Private tax-document vault | Planned | Documents have user ownership, permissions and tags |
| ☐ | FIN-078 | Tax reporting period handling | Planned | Supports historic FY/AY and newer Tax Year convention |
| ☐ | FIN-079 | Form 16 upload and metadata extraction | Planned | Extracted fields are user-reviewable with source refs |
| ☐ | FIN-080 | AIS/TIS upload identification | Planned | User uploads and tags source files without unofficial scraping |
| ☐ | FIN-081 | Tax document checklist | Planned | Checklist based on declared applicable income sources |
| ☐ | FIN-082 | Tax readiness reasons and gaps | Planned | Score/status explain exactly which documents are missing |
| ☐ | FIN-083 | Verified official tax sources catalog | Planned | Every published change links to authoritative document |
| ☐ | FIN-084 | Versioned rule metadata store | Planned | Effective dates, publication and verification fields captured |
| ☐ | FIN-085 | Rule review and approval workflow | Planned | Unapproved rule changes cannot affect user output |
| ☐ | FIN-086 | Tax policy change history and rollback | Planned | Reviewer actions and older rules remain inspectable |
| ☐ | FIN-087 | Source-linked tax knowledge viewer | Planned | Users can see applicable sourced changes by period |
| ☐ | FIN-088 | Professional reviewer sign-off | Planned | Tax content marked verified only after qualified review |
| ☐ | FIN-089 | Tax limitations disclosure | Planned | Tax estimates and filing not falsely advertised as available |


## V1 — CA sharing pilot

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-090 | Exportable CA-ready report | Planned | Annual summary plus issues/missing documents included |
| ☐ | FIN-091 | User consent before CA sharing | Planned | Explicit selected-document sharing scopes available |
| ☐ | FIN-092 | Time-limited access invite | Planned | Invitation expires and uses secure access process |
| ☐ | FIN-093 | Revoke access immediately | Planned | Revoked professional cannot fetch resources |
| ☐ | FIN-094 | CA viewer with least privilege | Planned | CA sees only authorized package content |
| ☐ | FIN-095 | Share access audit trail | Planned | User can review share and access events |
| ☐ | FIN-096 | CA identity and invite abuse controls | Planned | Invite cannot be used by unintended recipients |


## V1 — Billing and monetization

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-097 | Entitlement matrix | Planned | Free/Plus/Tax Pack permissions enforce server-side |
| ☐ | FIN-098 | Usage-limited free plan | Planned | API rejects exceeded free allowances |
| ☐ | FIN-099 | Checkout integration | Planned | Paid checkout returns to verified order status |
| ☐ | FIN-100 | Signed payment webhooks | Planned | Invalid webhook signatures are rejected |
| ☐ | FIN-101 | Idempotent payment event handling | Planned | Duplicate webhooks don't duplicate entitlements |
| ☐ | FIN-102 | Upgrade and downgrade | Planned | User can change plan without inconsistent balances |
| ☐ | FIN-103 | Refund and cancel workflow | Planned | Refund/cancellation semantics documented and tested |
| ☐ | FIN-104 | Receipts/invoice information | Planned | Required payment records accessible |
| ☐ | FIN-105 | Failed payment handling | Planned | Incomplete purchase never unlocks paid rights |
| ☐ | FIN-106 | Pricing and paywall UX | Planned | Feature pricing understandable before payment |
| ☐ | FIN-107 | Revenue and conversion telemetry | Planned | Metrics exclude sensitive user transaction content |


## V1 — Security privacy compliance

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-108 | Data minimization policy | Planned | Financial PII not sent to analytics/logs by default |
| ☐ | FIN-109 | Encryption in transit and at rest | Planned | Managed encryption and TLS configured |
| ☐ | FIN-110 | Fine-grained authorization | Planned | Cross-account and CA scopes verified in API tests |
| ☐ | FIN-111 | Secrets manager and key rotation approach | Planned | Secret values are never committed |
| ☐ | FIN-112 | Private storage + signed reads | Planned | No public bucket or guessable files |
| ☐ | FIN-113 | Upload malware and content checks | Planned | Suspicious files quarantined/rejected |
| ☐ | FIN-114 | Import processor isolation | Planned | Untrusted PDFs cannot execute arbitrary code |
| ☐ | FIN-115 | Privacy notice and opt-in consent | Planned | Data use documented and required consents recorded |
| ☐ | FIN-116 | Data export function | Planned | User can export own data safely |
| ☐ | FIN-117 | Deletion request function | Planned | Data removed or retained according to documented policy |
| ☐ | FIN-118 | Session/device security | Planned | Privileged sessions handled securely |
| ☐ | FIN-119 | Audit logging and retention | Planned | Sensitive operations logged without raw documents |
| ☐ | FIN-120 | Abuse prevention and throttling | Planned | Expensive AI and auth endpoints rate-limited |
| ☐ | FIN-121 | Security dependency scanning | Planned | CI scans dependencies and secrets |
| ☐ | FIN-122 | Automated backup and restore test | Planned | Restore exercise succeeds from backup |
| ☐ | FIN-123 | Incident response guide and contact | Planned | Operational roles and escalation steps documented |
| ☐ | FIN-124 | Legal/privacy review gate | Planned | External professional review before real-data release |
| ☐ | FIN-125 | External security review gate | Planned | No unresolved critical/high issues before launch |
| ☐ | FIN-126 | Third-party processor register | Planned | AI, email, hosting and payment processors documented |


## V1 — Infrastructure quality operations

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-127 | Modular monolith and DB migrations | Planned | APIs and migrations reproducible from clean checkout |
| ☐ | FIN-128 | CI test/lint/typecheck | Planned | Every PR blocks on core checks |
| ☐ | FIN-129 | Staging and production separation | Planned | No shared sensitive database or secrets |
| ☐ | FIN-130 | Background job reliability | Planned | Retries, dead-letter and error visibility working |
| ☐ | FIN-131 | Financial fixture regression suite | Planned | Golden expected-output fixtures included |
| ☐ | FIN-132 | Integration tests import-to-dashboard | Planned | Test flows run in CI |
| ☐ | FIN-133 | E2E smoke and billing tests | Planned | Sandbox flow validated on every release |
| ☐ | FIN-134 | Monitoring and error alerts | Planned | Logs and exceptions reach configured owner |
| ☐ | FIN-135 | Observability privacy guards | Planned | Logging fields are sanitized and sampled |
| ☐ | FIN-136 | Performance load tests | Planned | Upload and query p95 budgets defined and checked |
| ☐ | FIN-137 | Deployment rollback runbook | Planned | Rollback and DB migration safety documented |
| ☐ | FIN-138 | Data recovery exercise | Planned | Backups restore readable user records |
| ☐ | FIN-139 | Product support ticketing | Planned | Report-problem workflow hides customer financial data by default |
| ☐ | FIN-140 | Accessibility and mobile-responsive web | Planned | Core flows usable keyboard/mobile |
| ☐ | FIN-141 | Public help/FAQ and known formats list | Planned | Users see supported file formats and limitations |
| ☐ | FIN-142 | Release approval checklist | Planned | Launch gates tracked and blockers prevent launch |
| ☐ | FIN-143 | Automated GitHub feature tracking | Planned | Issues drive checklist CSV/XLSX and progress docs |
| ☐ | FIN-144 | Brand-rename configuration | Planned | Display name can change without changing stable IDs |


## V1.5 — Expanded personal finance

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-145 | Additional bank adapters | Planned | Most demanded banks tested with customer fixtures |
| ☐ | FIN-146 | More credit card formats | Planned | Additional supported card parsers with reconciliation |
| ☐ | FIN-147 | Goals and budgeting | Planned | Optional goals calculated from user-confirmed inputs |
| ☐ | FIN-148 | Manual asset and liability records | Planned | Cash, deposits and loans captured as manual data |
| ☐ | FIN-149 | Coverage-aware net-worth summary | Planned | Explicit inclusion/exclusion of manually entered sources |
| ☐ | FIN-150 | Family household view | Planned | Opt-in shared finances with role boundaries |
| ☐ | FIN-151 | Notification preference center | Planned | Email/app notification channel controls |
| ☐ | FIN-152 | Improved merchant classifier | Planned | User-corrected patterns used with privacy controls |
| ☐ | FIN-153 | Subscription reminder automation | Planned | Reminder schedule based on verified recurring transactions |
| ☐ | FIN-154 | Localization for Indian languages | Planned | Accessibility-checked translations for selected languages |


## V2 — Advanced tax intelligence

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-155 | Professionally verified tax calculation engine | Planned | Tax-year/regime calculation suite independently verified |
| ☐ | FIN-156 | Tax regime comparison | Planned | Applicable tax regimes compared by verified rules |
| ☐ | FIN-157 | Capital gains statement normalization | Planned | Supported broker statements normalized with traceability |
| ☐ | FIN-158 | Salary and other income reconciliation | Planned | User+CA can inspect tax-income classifications |
| ☐ | FIN-159 | Personalized policy relevance engine | Planned | Rule-change notices filtered to declared circumstances |
| ☐ | FIN-160 | Estimated tax payment/TDS summary | Planned | Tax payments and deductions shown with verified source data |
| ☐ | FIN-161 | Tax notices and deadline organizer | Planned | User-supplied notice/reminders organized safely |
| ☐ | FIN-162 | CA reviewer collaboration on tax issues | Planned | Dedicated query and resolution workflow |
| ☐ | FIN-163 | Historical tax position reproducibility | Planned | Re-run stored inputs against pinned rules versions |


## V2 — CA workspace SaaS

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-164 | CA practice signup and verification | Planned | Professional account verification process designed |
| ☐ | FIN-165 | Firm-level staff roles | Planned | Firm data segregated and permissioned |
| ☐ | FIN-166 | Client invitation and intake workflows | Planned | Client joins with explicit consent |
| ☐ | FIN-167 | Document requests and reminders | Planned | User receives scoped requests and uploads |
| ☐ | FIN-168 | Client readiness pipeline | Planned | Firm can filter missing docs and open issues |
| ☐ | FIN-169 | Multi-client secure document dashboard | Planned | Professional sees only authorized clients |
| ☐ | FIN-170 | CA comments and client review tasks | Planned | Threaded client-specific workflow |
| ☐ | FIN-171 | Client tax package assembly | Planned | Accountant can review/edit package generation |
| ☐ | FIN-172 | Activity and compliance audit reports | Planned | Firm access trails exportable to authorized admins |
| ☐ | FIN-173 | Firm subscription tiers | Planned | Billing and seat/client count handled correctly |
| ☐ | FIN-174 | Client relationship revoke/export | Planned | User retains control and can remove practice access |


## V3+ — Future regulated integrations

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-175 | Account Aggregator integration through eligible regulated arrangements | Planned | Consent-based bank feeds only after regulatory review |
| ☐ | FIN-176 | Direct Income Tax ERI flow | Planned | Integration available only with applicable authorized status |
| ☐ | FIN-177 | Broker API/holdings integration | Planned | Approved customer authorization and data sharing |
| ☐ | FIN-178 | GST/ASP-GSP partner integrations | Planned | GST flows use suitable provider and consent |
| ☐ | FIN-179 | Authorized PAN verification | Planned | Provider/legal access confirmed |
| ☐ | FIN-180 | Automated financial sync scheduling | Planned | Only permitted integrations and revocable consent |
| ☐ | FIN-181 | Personalized investment advice with registered providers | Planned | Advice offered only through properly licensed service |
| ☐ | FIN-182 | Direct tax return submission | Planned | Authorized ERI and professional review path |


## Future — Long-term product expansion

| Check | ID | Feature | Status | Acceptance |
| --- | --- | --- | --- | --- |
| ☐ | FIN-183 | Family financial vault | Planned | Secure household document sharing and nominee records |
| ☐ | FIN-184 | Freelancer invoice and expense workflows | Planned | Separate personal/business money context |
| ☐ | FIN-185 | Sole proprietor cash flow reports | Planned | Tax-ready business income and expenses |
| ☐ | FIN-186 | Business bookkeeping export | Planned | Accounting software-compatible exports |
| ☐ | FIN-187 | CA marketplace discovery | Planned | Ethics and referral compliance reviewed before monetization |
| ☐ | FIN-188 | Professional financial adviser connections | Planned | Registered advisers listed with clear role boundaries |
| ☐ | FIN-189 | Insurance renewal/coverage organizer | Planned | Reminder and vault, no unlicensed product sale |
| ☐ | FIN-190 | Loans and debt payoff scenarios | Planned | Calculators without loan origination initially |
| ☐ | FIN-191 | International and multicurrency statements | Planned | Exchange rates and multi-entity rules validated |
| ☐ | FIN-192 | Native Android and iOS | Planned | Mobile releases after web retention demonstrates demand |
| ☐ | FIN-193 | Third-party user-authorized integrations | Planned | Explicit permissions and revocation |
| ☐ | FIN-194 | Financial education library | Planned | Verified explainers with policy revision history |


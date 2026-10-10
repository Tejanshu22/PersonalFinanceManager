"""One-time manifest authoring helper. Not part of the automatic progress workflow."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
features=[]
def add(cat, release, day, entries):
    for item in entries.splitlines():
        item=item.strip()
        if not item or item.startswith('#'): continue
        parts=item.split(' | ')
        if len(parts)!=2: raise ValueError((cat,item))
        name,accept=parts
        number=len(features)+1
        features.append({
          'id':f'FIN-{number:03d}', 'category':cat, 'name':name,
          'release':release, 'priority':'P0' if release=='V1' and day <= 65 else ('P1' if release=='V1' else 'P2'),
          'target_day':day if release=='V1' else None,
          'acceptance':accept,
          'owner':'Unassigned',
        })

add('Discovery & product', 'V1', 1, '''
Define persona and measurable problem | Signed-off V1 product brief with exclusions and success metrics
Customer discovery interviews | At least 10 interviews summarized with evidence and insights
CA workflow discovery | At least two professional workflow interviews documented
Competitor and pricing research | Comparison and tested price hypotheses recorded
Brand configuration and rename policy | Display name comes only from config and rebrand guide exists
Landing page and waitlist | Privacy-conscious waitlist and signup flow works
Product acceptance criteria | V1 functions have explicit pass/fail conditions
Risk register and decision log | Major assumptions and risks have owners and follow-ups
''')
add('Identity & onboarding', 'V1', 8, '''
Secure sign-up and login | Signup, login and logout tested end to end
Verified email onboarding | User email verification works
Password reset and session revocation | Reset and revoked sessions cannot access accounts
Financial account profile | User can create and manage owned bank/card account metadata
Income-type onboarding | Salary, freelance, investment and other income types selected
Preferences and reporting timezone | Reporting window and timezone persisted correctly
Sensitive session management | Expired/revoked sessions are rejected server-side
Onboarding tutorial and empty states | No-data users see correct next steps, not fake numbers
''')
add('Import & document ingestion', 'V1', 14, '''
CSV import with column mapping | Supported CSV imports with preview and schema checks
Money amount and debit-credit normalization | Negative/positive and debit/credit variants normalized
Date parsing and timezone semantics | Dates parsed consistently with stated date assumptions
Canonical statement model | Each import preserves source, period and ownership
Import queue and progress indicator | Async jobs show pending, success, partial failure and error
File type/size limits | Unsupported or oversized files rejected safely
Secure upload and temporary download URLs | Unauthorized users cannot read uploaded files
Password-protected PDFs handled safely | Password is ephemeral and never logged or stored
PDF parser framework | Bank-specific parser adapters run in isolated workflow
Supported bank PDF parser #1 | Confirmed fixture suite passes
Supported bank PDF parser #2 | Confirmed fixture suite passes
Supported card statement parser #1 | Credit-card purchases, repayments, fees and refunds classified
Manual import preview and confirmation | Imported rows not persisted as final without validation path
Unsupported format guidance | Clear fallbacks and support request available
Partial extraction warnings | Missing pages/rows are surfaced explicitly
Statement reconciliation | Where balances exist, integrity checks flag discrepancies
Re-import and overlap handling | Re-import does not double-count rows
Raw source traceability | Every transaction links to source statement reference
''')
add('Transaction data quality', 'V1', 19, '''
Normalized transaction ledger | Decimal amount, account and source metadata stored
Deterministic merchant recognition | Merchant rules identify common narrations
Rules-first categorization engine | Transparent category decisions for known patterns
User transaction editing | Manual edits persist and show audit history
User-defined category rules | Repeated merchant fixes become scoped rules
Internal transfer candidate matching | Own-account transfers are not counted as income/spend
Refund and reversal detection | Refunds reverse appropriate spending without fake income
Credit-card repayment treatment | Bank-to-card repayments don't inflate spending
Duplicate row identification | Same rows are ignored on overlapping uploads
Uncertain classification queue | Low-confidence classifications require user review
Transaction classification provenance | Original text and reason/confidence retained
Transaction correction undo | User can reverse a mistaken category edit
Source totals mismatch handling | Reports show unreconciled data warnings
''')
add('Financial calculations & dashboard', 'V1', 33, '''
Income and actual spending rules | Salary, refund, investments and transfer separation validated
Month-by-month cash flow | Correct monthly inflows/outflows shown by account/period
Investment-contribution metric | Investments tracked separately from consumption spending
Category breakdowns | Charts match canonical transactions
Merchant breakdowns | Merchant totals trace back to rows
Cross-account summary | Combined view excludes internal transfer double count
Time-period and account filters | All analytics respect selected filters
Historical comparison | Period-on-period comparison uses comparable coverage
Data coverage/freshness warnings | Last import and missing statement periods shown
Transaction drill-down | Every aggregate opens supporting transactions
Empty/partial-data behavior | Insufficient data does not generate false precision
''')
add('Personal finance insights', 'V1', 39, '''
Recurring-charge detector | Repeated merchant-period sequences produce candidates
Subscriptions and fixed commitments view | Recurring monthly/annual values displayed
Potential duplicate payment alerts | Suspected duplicate charges are clearly labeled as tentative
Unusual spending alerts | Outliers are flagged without fraud accusations
Recurring price-increase alerts | Meaningful increase compared with prior payments detected
Explainable savings metrics | Cash available and invested cash explicitly distinguished
Monthly financial summary report | Monthly report produced from audited calculations
Coverage-aware health components | Components show evidence and avoid fake overall score
Upload reminder and monthly notification preferences | User controls reminder frequency and channel
''')
add('Ask My Money AI', 'V1', 43, '''
Approved financial query tools | Model cannot access DB except via allowlisted functions
Safe question-to-tool routing | Spending, income and comparison intents map correctly
Financial chat interface | Users can ask questions with usable failure messages
Source-backed numerical answers | Every number is derived from backend and traceable
Privacy-minimized model prompts | PAN/account numbers and unrelated financial rows withheld
Prompt injection resilience | Untrusted statement texts cannot override system behavior
Ambiguity and missing data responses | AI acknowledges incomplete account coverage
AI usage limits and cost controls | Server enforces quotas and protects expensive endpoints
AI evaluation set | Numerical, redaction and adversarial tests pass
''')
add('Tax readiness and policy', 'V1', 51, '''
Private tax-document vault | Documents have user ownership, permissions and tags
Tax reporting period handling | Supports historic FY/AY and newer Tax Year convention
Form 16 upload and metadata extraction | Extracted fields are user-reviewable with source refs
AIS/TIS upload identification | User uploads and tags source files without unofficial scraping
Tax document checklist | Checklist based on declared applicable income sources
Tax readiness reasons and gaps | Score/status explain exactly which documents are missing
Verified official tax sources catalog | Every published change links to authoritative document
Versioned rule metadata store | Effective dates, publication and verification fields captured
Rule review and approval workflow | Unapproved rule changes cannot affect user output
Tax policy change history and rollback | Reviewer actions and older rules remain inspectable
Source-linked tax knowledge viewer | Users can see applicable sourced changes by period
Professional reviewer sign-off | Tax content marked verified only after qualified review
Tax limitations disclosure | Tax estimates and filing not falsely advertised as available
''')
add('CA sharing pilot', 'V1', 57, '''
Exportable CA-ready report | Annual summary plus issues/missing documents included
User consent before CA sharing | Explicit selected-document sharing scopes available
Time-limited access invite | Invitation expires and uses secure access process
Revoke access immediately | Revoked professional cannot fetch resources
CA viewer with least privilege | CA sees only authorized package content
Share access audit trail | User can review share and access events
CA identity and invite abuse controls | Invite cannot be used by unintended recipients
''')
add('Billing and monetization', 'V1', 62, '''
Entitlement matrix | Free/Plus/Tax Pack permissions enforce server-side
Usage-limited free plan | API rejects exceeded free allowances
Checkout integration | Paid checkout returns to verified order status
Signed payment webhooks | Invalid webhook signatures are rejected
Idempotent payment event handling | Duplicate webhooks don't duplicate entitlements
Upgrade and downgrade | User can change plan without inconsistent balances
Refund and cancel workflow | Refund/cancellation semantics documented and tested
Receipts/invoice information | Required payment records accessible
Failed payment handling | Incomplete purchase never unlocks paid rights
Pricing and paywall UX | Feature pricing understandable before payment
Revenue and conversion telemetry | Metrics exclude sensitive user transaction content
''')
add('Security privacy compliance', 'V1', 69, '''
Data minimization policy | Financial PII not sent to analytics/logs by default
Encryption in transit and at rest | Managed encryption and TLS configured
Fine-grained authorization | Cross-account and CA scopes verified in API tests
Secrets manager and key rotation approach | Secret values are never committed
Private storage + signed reads | No public bucket or guessable files
Upload malware and content checks | Suspicious files quarantined/rejected
Import processor isolation | Untrusted PDFs cannot execute arbitrary code
Privacy notice and opt-in consent | Data use documented and required consents recorded
Data export function | User can export own data safely
Deletion request function | Data removed or retained according to documented policy
Session/device security | Privileged sessions handled securely
Audit logging and retention | Sensitive operations logged without raw documents
Abuse prevention and throttling | Expensive AI and auth endpoints rate-limited
Security dependency scanning | CI scans dependencies and secrets
Automated backup and restore test | Restore exercise succeeds from backup
Incident response guide and contact | Operational roles and escalation steps documented
Legal/privacy review gate | External professional review before real-data release
External security review gate | No unresolved critical/high issues before launch
Third-party processor register | AI, email, hosting and payment processors documented
''')
add('Infrastructure quality operations', 'V1', 74, '''
Modular monolith and DB migrations | APIs and migrations reproducible from clean checkout
CI test/lint/typecheck | Every PR blocks on core checks
Staging and production separation | No shared sensitive database or secrets
Background job reliability | Retries, dead-letter and error visibility working
Financial fixture regression suite | Golden expected-output fixtures included
Integration tests import-to-dashboard | Test flows run in CI
E2E smoke and billing tests | Sandbox flow validated on every release
Monitoring and error alerts | Logs and exceptions reach configured owner
Observability privacy guards | Logging fields are sanitized and sampled
Performance load tests | Upload and query p95 budgets defined and checked
Deployment rollback runbook | Rollback and DB migration safety documented
Data recovery exercise | Backups restore readable user records
Product support ticketing | Report-problem workflow hides customer financial data by default
Accessibility and mobile-responsive web | Core flows usable keyboard/mobile
Public help/FAQ and known formats list | Users see supported file formats and limitations
Release approval checklist | Launch gates tracked and blockers prevent launch
Automated GitHub feature tracking | Issues drive checklist CSV/XLSX and progress docs
Brand-rename configuration | Display name can change without changing stable IDs
''')

# Near-term follow-on work (not initial paid MVP)
add('Expanded personal finance', 'V1.5', 0, '''
Additional bank adapters | Most demanded banks tested with customer fixtures
More credit card formats | Additional supported card parsers with reconciliation
Goals and budgeting | Optional goals calculated from user-confirmed inputs
Manual asset and liability records | Cash, deposits and loans captured as manual data
Coverage-aware net-worth summary | Explicit inclusion/exclusion of manually entered sources
Family household view | Opt-in shared finances with role boundaries
Notification preference center | Email/app notification channel controls
Improved merchant classifier | User-corrected patterns used with privacy controls
Subscription reminder automation | Reminder schedule based on verified recurring transactions
Localization for Indian languages | Accessibility-checked translations for selected languages
''')
add('Advanced tax intelligence', 'V2', 0, '''
Professionally verified tax calculation engine | Tax-year/regime calculation suite independently verified
Tax regime comparison | Applicable tax regimes compared by verified rules
Capital gains statement normalization | Supported broker statements normalized with traceability
Salary and other income reconciliation | User+CA can inspect tax-income classifications
Personalized policy relevance engine | Rule-change notices filtered to declared circumstances
Estimated tax payment/TDS summary | Tax payments and deductions shown with verified source data
Tax notices and deadline organizer | User-supplied notice/reminders organized safely
CA reviewer collaboration on tax issues | Dedicated query and resolution workflow
Historical tax position reproducibility | Re-run stored inputs against pinned rules versions
''')
add('CA workspace SaaS', 'V2', 0, '''
CA practice signup and verification | Professional account verification process designed
Firm-level staff roles | Firm data segregated and permissioned
Client invitation and intake workflows | Client joins with explicit consent
Document requests and reminders | User receives scoped requests and uploads
Client readiness pipeline | Firm can filter missing docs and open issues
Multi-client secure document dashboard | Professional sees only authorized clients
CA comments and client review tasks | Threaded client-specific workflow
Client tax package assembly | Accountant can review/edit package generation
Activity and compliance audit reports | Firm access trails exportable to authorized admins
Firm subscription tiers | Billing and seat/client count handled correctly
Client relationship revoke/export | User retains control and can remove practice access
''')
add('Future regulated integrations', 'V3+', 0, '''
Account Aggregator integration through eligible regulated arrangements | Consent-based bank feeds only after regulatory review
Direct Income Tax ERI flow | Integration available only with applicable authorized status
Broker API/holdings integration | Approved customer authorization and data sharing
GST/ASP-GSP partner integrations | GST flows use suitable provider and consent
Authorized PAN verification | Provider/legal access confirmed
Automated financial sync scheduling | Only permitted integrations and revocable consent
Personalized investment advice with registered providers | Advice offered only through properly licensed service
Direct tax return submission | Authorized ERI and professional review path
''')
add('Long-term product expansion', 'Future', 0, '''
Family financial vault | Secure household document sharing and nominee records
Freelancer invoice and expense workflows | Separate personal/business money context
Sole proprietor cash flow reports | Tax-ready business income and expenses
Business bookkeeping export | Accounting software-compatible exports
CA marketplace discovery | Ethics and referral compliance reviewed before monetization
Professional financial adviser connections | Registered advisers listed with clear role boundaries
Insurance renewal/coverage organizer | Reminder and vault, no unlicensed product sale
Loans and debt payoff scenarios | Calculators without loan origination initially
International and multicurrency statements | Exchange rates and multi-entity rules validated
Native Android and iOS | Mobile releases after web retention demonstrates demand
Third-party user-authorized integrations | Explicit permissions and revocation
Financial education library | Verified explainers with policy revision history
''')

assert len({f['id'] for f in features})==len(features)
(ROOT/'data'/'features.json').write_text(json.dumps(features,indent=2,ensure_ascii=False)+'\n')
print('FEATURES', len(features), 'V1', sum(f['release']=='V1' for f in features))

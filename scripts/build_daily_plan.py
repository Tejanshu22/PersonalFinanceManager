"""One-time daily plan seed from reviewed 85-day schedule."""
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'data'/'daily_plan.json'
weekly=[
('Research and requirements', [
'Freeze V1 scope, personas and measurable success criteria',
'Interview five salaried prospective users and summarize buying pain',
'Interview five more prospects and two CAs; identify reviewer',
'Analyze competitors, pricing, compliance risks and name conflicts',
'Create user journeys, wireframes, landing page and waitlist']),
('Architecture and secure foundations', [
'Scaffold Next.js, FastAPI, PostgreSQL, CI and local staging',
'Design canonical ledger, ownership, Decimal amounts and migrations',
'Implement secure authentication and session recovery',
'Build private file uploads, scanning and async job infrastructure',
'Implement audit events, monitoring, environment isolation and threat model']),
('First CSV importer', [
'Canonical transaction/account/source data contract',
'CSV upload with flexible column matching',
'Normalize dates, amounts and narration safely',
'Async import workflow with row-level error recovery',
'Import preview and user approve/reject experience']),
('Categorization and correctness', [
'Deduplication and idempotent transaction imports',
'Merchant normalization and classification rules',
'Own-account transfer, refunds, reversals and card payment logic',
'Corrections, edit history, scoped user-defined rules',
'Golden fixtures and accounting edge-case tests']),
('PDF and card statements', [
'PDF framework, parser isolation, file limits and ephemeral passwords',
'Bank-specific PDF parser #1 with tests',
'Format variants and regression tests for first bank parser',
'Credit-card statement adapter with purchase/payment/refund logic',
'Extraction preview and reconciliation warnings']),
('Data pipeline hardening', [
'Bank-specific PDF parser #2',
'Unsupported-format handling and manual fallback UX',
'Overlapping statement periods and reconciliation rules',
'Job retry, failure analytics and duplicate protection',
'Alpha test on anonymized fixtures; fix blocking parser bugs']),
('Financial dashboard', [
'Specify and implement income, spending and investment metrics',
'Category/merchant trends and reliable aggregation APIs',
'Build responsive dashboard with live imported data',
'Last-import timestamps, partial coverage labels and drill-down',
'Validate totals against independent calculations']),
('Recurring intelligence', [
'Recurring-charge detection heuristics',
'Subscription and commitments dashboard',
'Duplicate and unusual-spend alert candidates',
'Monthly report builder with supporting details',
'Health metric components with coverage restrictions']),
('AI money assistant', [
'Allowlisted AI financial tool interface with no arbitrary SQL',
'Question routing and deterministic tool results',
'AI chat UI and usage limits',
'Source-backed answers, prompt redaction and traceability',
'Adversarial and numeric test corpus including prompt injection']),
('Tax-document foundation', [
'Private tax vault and document metadata',
'Historic FY/AY plus new Tax Year data model',
'Form 16 upload and reviewed fields',
'AIS/TIS upload workflow and document tagging',
'Income-specific tax-readiness and missing-document checks']),
('Policy and expert review', [
'Versioned tax-rule metadata with source/effective date',
'Policy admin entry, review and publish workflow',
'Historic source linking and rule-set applicability',
'Audit, rollback and protected publication process',
'Qualified tax-expert check of supported content and examples']),
('CA collaboration', [
'Generate accountant-ready annual financial package',
'Explicit limited-scope consent for CA sharing',
'Time-limited invitation and scoped CA access',
'Revocation, expiry and access audit tests',
'End-to-end beta integration test and feature freeze']),
('Billing', [
'Plan and entitlements model with backend-enforced limits',
'Payment checkout and paid-order verification',
'Webhook signature checks, replay and idempotency tests',
'Refunds, failed payments, receipts and cancellations',
'Pricing/upgrade/paywall UX and sandbox billing rehearsal']),
('Legal and operational hardening', [
'Consent and privacy controls in app',
'User data exports, deletion requests and retention policies',
'Legal review of privacy, terms, cancellation and disclaimers',
'Support workflow and incident escalation',
'Automated security checks and remediation list']),
('Release candidate', [
'Full integration/E2E regression and authorization tests',
'Financial correctness and all supported format fixtures',
'Concurrency/performance and robustness tests',
'Restore backups and incident recovery rehearsal',
'Independent security assessment and fix gating']),
('Controlled paid beta', [
'Invite limited consenting users after release gate',
'Assess import quality, corrections and user comprehension',
'Test real early payments and refunds in controlled rollout',
'Interview paid/free beta testers and solve biggest problems',
'Document support, onboarding and production rollout']),
('Public launch', [
'Fix high-priority testing and feedback findings',
'Final end-to-end, auth, tax-policy and billing regression',
'Verify production alerts, recovery and rollback',
'Full release rehearsal and go/no-go decision',
'Limited public launch if all security and accuracy gates pass'])
]
assert len(weekly)==17
rows=[]
for wi,(phase,tasks) in enumerate(weekly):
    for pos,task in enumerate(tasks):
        day=wi*5+pos+1
        rows.append({'id':f'DAY-{day:03d}', 'day':day, 'week':wi+1,'phase':phase,'task':task,'acceptance':'Reviewed work artifact or documented validation evidence', 'owner':'Unassigned'})
assert len(rows)==85
p.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n')
print('DAYS',len(rows))

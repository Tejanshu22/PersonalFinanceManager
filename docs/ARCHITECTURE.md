# FINNest — architecture and foundation status

**DAY-001 review draft · 2026-10-10.** This describes requirements and dependencies, not deployed components. [Decisions](DECISIONS.md) separates approved boundaries from unresolved choices.

**DAY-006 update · 2026-10-12:** the [local foundation](DAY_06_FOUNDATION.md) now implements Next.js App Router/TypeScript UI sections, a bounded canvas adapter, exact synthetic selectors, a FastAPI monolith entry point with health probes and PostgreSQL/Compose staging. The remaining domain architecture below is still proposed. No ledger schema, migrations, authentication, upload/storage pipeline or production deployment is claimed. Browser sample data has no API dependency; local readiness exercises the API-to-PostgreSQL boundary. Branding is loaded by the server shell from central config. New application CI is separate from the unchanged tracker workflow.

## Shape and trust boundaries

**DAY-007 implementation · 2026-10-13:** [ledger implementation and evidence](DAY_07_LEDGER.md) records eight owner-scoped PostgreSQL tables, an environment-configured Alembic migration, SQLAlchemy Core/psycopg repository, strict Decimal validation, immutable provenance, append-only corrections, concurrency-guarded relationships and coverage-qualified aggregates. O-04 is founder-approved for synthetic development; independent professional/security review remains pending. The migration has run only in a guarded disposable test database. The health-only API, ordinary staging database and fictional UI remain unchanged; no production identity or financial API is implied.

Retain the proposed responsive Next.js/TypeScript frontend, FastAPI/Pydantic modular monolith, PostgreSQL exact numeric storage, private S3-compatible objects and isolated background workers. Redis/queue technology is needed only where justified by reliable job execution; do not introduce microservices or additional infrastructure without evidence.

```text
Browser -> authenticated API -> owner-scoped ledger / metadata in PostgreSQL
                 |
                 +-> private quarantine -> scanner -> isolated parser worker
                 |                                      |
                 |                           preview / reconciliation / correction
                 |                                      |
                 +-> deterministic analytics <--- canonical ledger
                 |          |
                 |          +-> report snapshots and approved aggregate tools -> LLM
                 +-> reviewed tax metadata -> readiness reasons
                 +-> scoped CA authorization gateway -> selected package/documents
                 +-> hosted checkout <-> signed events -> entitlement state

All stores, caches, jobs, exports and backups participate in retention/deletion.
```

Ownership checks occur in the API and workers; neither model-generated arguments nor browser IDs establish authority. Use a user/account/document ownership model and an explicit share grant, not a single client-supplied user filter. Privileged policy publishing and support access use separate restricted roles.

## Data and processing contracts

- Preserve immutable source values, document hash/provenance, parser version, period, currency, import identity and extraction location. Corrections are additional auditable records; immutability is not a reason to retain data forever after an approved deletion request.
- Separate cash accounts and credit-card liability activity. Model matched transfers/refunds/repayments as relationships between preserved rows. Keep unknown categories and missing counterparts explicit.
- Use exact numeric database columns and decimal arithmetic end to end; future API money values must avoid binary floating-point conversion. O-04 now approves positive INR magnitude with debit/credit, strict paise validation and posted dates for synthetic implementation; its limits and external-review boundary are in the Day 7 report.
- Import states distinguish quarantined, processing, awaiting review, finalized, partial, rejected and failed. Retry with stable job/import identity and transactional finalization; no duplicate ledger writes. User acknowledgment cannot erase a reconciliation failure.
- Analytics use versioned deterministic functions and explicit account/period coverage. Report snapshots pin input/correction/calculation versions; new corrections create a new report version. Tax-ready exports include unresolved issues and applicable metadata rather than pretending full financial coverage.
- AI receives minimal approved structured results and opaque citation identifiers; owner-scoped UI drill-down resolves references. No unrestricted SQL, full financial-document retrieval, untrusted narration in prompts or autonomous mutation of financial records.
- Tax publication may begin as a small protected review workflow. Preserve reviewer identity, source/applicability, versions and rollback; a large content-management system is not required to satisfy governance.
- CA sharing uses selected snapshot resources and request-time authorization. Private signed storage reads may be used internally, but recipient-visible URLs must not bypass revocation.
- Persist verified payment events and explicit entitlement state transitions atomically; retries/out-of-order delivery must converge safely. Browser checkout success is not proof of payment.
- Deletion coordinates database, objects, derivatives, jobs, caches, shares and processors, with a deletion ledger applied during backup restore. Implement an export that includes user records, provenance and corrections.

## Dependency plan: ordering proposal, not an edited roadmap

| Stage | Must exist before dependent work | Scheduling impact requiring separate reconciliation |
| --- | --- | --- |
| Discovery / Days 1–5 | Personas, safe interview process, initial financial definitions, format-fixture candidates, reviewer availability, processor/retention decisions | Recruit tax/legal/security reviewers early instead of first arranging review near launch |
| Secure foundation / Days 6–10 | Identity/ownership, migrations, private quarantine, scanner/isolation, secrets, minimal audit, consent checks, fixture harness and CI | Move privacy implementation and security-critical controls ahead of any real-data ingestion |
| Ingestion / Days 11–30 | Approved schema/equations and golden expectations before parser output; retry/overlap/access tests from first adapter | Reuse proposed second-adapter capacity for first-format quality, deletion/export and pipeline recovery; exact DAY edits pending |
| Analytics / Days 31–40 | Reviewed financial semantics, correction history, coverage and independent totals | Reuse deferred health/reminder/price-alert effort for test coverage and privacy lifecycle work; no silent scope additions |
| AI, tax and sharing / Days 41–59 | Minimal approved APIs; provider review; reviewed checklist rules; scoped identity and revocation mechanism | Avoid discovering consent or ownership gaps after these modules are built |
| Day 60 | Internal functional beta on approved safe fixtures; known limitations recorded | Not feature-complete public V1 and not permission to collect customer statements |
| Days 61–75 | Billing, complete privacy lifecycle, integration/load/recovery evidence, external review and remediation | Day 75 security-reviewed release candidate is a target; review booking and remediation time are dependencies |
| Days 76–80 | Signed real-data release gate and controlled-cohort consent/support capacity | Controlled real-user beta only if safeguards have been verified |
| Day 85 | Controlled beta evidence, payment validation, final review and go/no-go | Public launch target; unresolved gates move the date |

Existing [daily manifest](../data/daily_plan.json) and [generated roadmap](ROADMAP.md) remain unchanged. This is ordering guidance; the owner must approve a concrete day/feature remapping before those sources change.

## Operational considerations and open choices

Use staging with synthetic data, separate production secrets, migration rollback/forward-repair plans, monitored jobs, bounded retries and visible failure states. Backup restore must include object/metadata consistency and deletion replay. Proposed performance/recovery budgets are in [requirements](REQUIREMENTS.md), awaiting review.

Auth/hosting/storage/queue/model/payment vendors, regions, spending ceilings, exact limits, retention durations, support procedures and stronger-authentication policy are not selected. Prefer managed services where cost and security review support the choice; no deployment, account provisioning or dependency installation is authorized by this draft. Keep UI branding in [configuration](../config/brand.json).

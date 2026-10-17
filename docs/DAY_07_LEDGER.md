# DAY-007 — canonical financial ledger implementation

**2026-10-13 · Implemented for founder code review, synthetic development only.** O-04 is founder-approved under the latest “O-04 Approval and Ledger Implementation” instruction. Professional financial, tax, legal, privacy and independent security reviews remain outstanding. The migration was applied only to an isolated disposable test database; ordinary staging remains unchanged. No public financial API, real uploads or dashboard integration was added.

## Scheduled scope and accepted baseline

The [daily manifest](../data/daily_plan.json) records DAY-007, day 7/week 2, phase **Architecture and secure foundations**, task **Design canonical ledger, ownership, Decimal amounts and migrations**, acceptance **Reviewed work artifact or documented validation evidence**, owner **Unassigned**. There is no explicit dependency or FIN mapping field in this row. The founder additionally requests implementation after material monetary decisions are approved.

The founder confirms Day 6 acceptance. `git fetch origin` verified merge commit `65eb8c4` on `origin/master`, merging PR #13 and including `441b6ef` (Docker remediation) and `acf7c90` (compact-browser fix). `git merge-base --is-ancestor acf7c90 origin/master` returned 0. The initial checkout was clean on `codex/day-006-docker-security`; dedicated branch `codex/day-007-canonical-ledger` was created from `origin/master`, without changing local master. Its default upstream was removed to avoid targeting master on a later push. No commits or pushes performed.

GitHub PR/check-run API requests failed with TLS handshake timeouts. Merge ancestry is confirmed through fetched Git objects; remote CI success is **not independently confirmed**. Current local regression evidence is below. Historical pending-acceptance statements in the [Day 6 report](DAY_06_FOUNDATION.md) describe earlier snapshots; they do not override the founder's present acceptance.

Related foundations, without remapping or completing features: FIN-020 (source/period/ownership), FIN-035 (Decimal ledger), FIN-040/041 (transfers/refunds), FIN-046 (undo), FIN-127 (migrations), plus future classification/reporting/security work. These retain their existing target days and releases. The 194 feature IDs, 85 days and approved scope remain unchanged.

## O-04: founder-approved for synthetic development

The founder explicitly approved the previously reviewed [O-04](DECISIONS.md) conventions and authorized implementation with strict validation, concurrency safeguards and synthetic-only testing. This records implementation authority, not professional validation or release approval.

| Choice | Implemented convention | Trade-off / consequence |
| --- | --- | --- |
| Currency | INR-only accounts and rows, with a currency column constrained to `INR`; reject unsupported currencies | Retains an explicit currency boundary; multi-currency needs a later migration and reviewed reporting rules, never implicit FX |
| Amount / range | Positive exact magnitude, >0 and <10^18 rupees; economically at most two fractional digits; explicit `debit` or `credit` | Equivalent value range to positive NUMERIC(20,2). Zero-value informational rows remain source-only. No inferred signed direction |
| Strict persistence | PostgreSQL `NUMERIC` with NOT NULL and checks `amount > 0 AND amount < 1000000000000000000 AND amount = trunc(amount, 2)` | Rejects non-paise values, NaN and infinities without coercing away evidence; requires explicit checks instead of a scale typmod |
| Input normalization | Python Decimal from validated text/Decimal only; reject floats, bools, nonfinite values, unsupported currency and nonzero sub-paise digits; normalize accepted values to `0.01` | `1.2300` becomes `1.23`, but `1.005` is rejected, never silently rounded. Preserve original text. Bounded input length and Decimal context/traps must prevent accidental rounding during sums |
| Reporting date | Posted date is required for canonical posting; transaction/value dates are preserved if supplied | Missing posted date remains source-only/needs review. No quiet fallback to transaction date |
| Time semantics | Statement date-only values remain PostgreSQL DATE; audit times use UTC TIMESTAMPTZ | Do not shift dates through timezone conversion. Future timestamp adapters must declare source zone; ambiguous source times require review. The internal report takes explicit inclusive start/end DATE values; January 1–31 is the same monthly set as [January 1, February 1) |
| Refunds and reversals | Linked, confirmed consumption refunds reduce consumption in the refund posting month; preserve original transaction and cross-period relationship | No silent rewriting of earlier reports; a month may show negative net consumption. Unmatched refunds are separate unresolved credits, not income. Non-consumption returns do not reduce consumption |
| Savings / coverage | Use “observed income less net consumption” only when declared account/period coverage and reconciliation support it and no material unresolved activity remains; otherwise return unavailable plus reasons | Never infer complete savings, cash balance or net worth. For Day 7 use the conservative rule: any unresolved row or coverage gap withholds the measure |

**Amount bound rationale:** retain the approved `0 < amount < 10^18` rupees, largest accepted value `999999999999999999.99`. This provides 18 integer digits plus paise, matching the useful positive range of NUMERIC(20,2), ample headroom for personal-finance source records and bounded arithmetic/input validation. It is a technical ceiling, not a claim that such transactions are normal or an import/business limit. Reducing or increasing it requires a new decision/migration; it has not been changed. Python normalizes accepted values to two decimal places, while PostgreSQL rejects nonzero sub-paise values without scale coercion. The derived metric's exact label is **observed income less net consumption**, never a claim of complete savings.

Technical verification: PostgreSQL's [numeric documentation](https://www.postgresql.org/docs/17/datatype-numeric.html) states that declared scale coerces input by rounding; unscaled NUMERIC does not. A read-only probe on local PostgreSQL 17.11 returned `1.005::numeric(20,2) = 1.01`, the proposed equality-to-truncation predicate was false, and `0.10::numeric + 0.20::numeric = 0.30`. This verifies the storage trade-off, not a migration or domain test. Source accessed 2026-10-12.

## Final implemented schema

Eight small tables; no general journal, double-entry engine, balance engine or identity provider. UUID identifiers are neutral internal IDs. All timestamps below use TIMESTAMPTZ. Unless marked optional, columns are NOT NULL. Foreign keys use NO ACTION (no cascading deletes), with mutation-denial triggers for immutable facts/history; a later reviewed purge workflow must explicitly coordinate source, history, links and backups.

```mermaid
erDiagram
    ledger_owner ||--o{ financial_account : owns
    financial_account ||--o{ ledger_source : has
    ledger_source ||--o{ source_row : preserves
    financial_account ||--o{ canonical_transaction : contains
    source_row ||--o| canonical_transaction : normalizes
    canonical_transaction ||--|{ classification_event : records
    canonical_transaction ||--o{ transaction_link : from
    canonical_transaction ||--o{ transaction_link : to
    financial_account ||--o{ account_coverage : qualifies
```

| Table | Actual columns | Constraints / meaning |
| --- | --- | --- |
| `ledger_owner` | `id UUID PK`, `created_at`, `write_version BIGINT` | Per-owner serialization counter and opaque owner reference; synthetic IDs only today. No email, passwords, sessions or public owner-creation endpoint. Day 8 maps verified identity to this ID |
| `financial_account` | `id UUID PK`, `owner_id UUID`, `kind TEXT`, `currency TEXT`, `label TEXT`, `created_at` | Kind `bank`, `cash` or `credit_card`; bounded user label, not account number. Owner FK; UNIQUE(owner_id,id); currency INR. Account facts are immutable today; archival is later lifecycle work |
| `ledger_source` | `id UUID PK`, `owner_id`, `account_id`, `source_key TEXT`, `format TEXT`, `parser_version TEXT`, `period_start DATE`, `period_end DATE`, `created_at` | Immutable source batch/statement metadata. UNIQUE(owner_id,account_id,source_key); composite account FK. Source key is a stable opaque synthetic/import identity, not a public filename; period_start <= period_end |
| `source_row` | `id UUID PK`, `owner_id`, `account_id`, `source_id`, `row_key TEXT`, `original_amount_text TEXT`, `original_direction_text TEXT`, `original_posted_date_text TEXT`, optional `original_transaction_date_text`, optional `original_value_date_text`, optional `original_description`, `created_at` | Immutable minimal source snapshot, never a raw PDF/PII dump. UNIQUE(owner_id,source_id,row_key); composite source FK includes account. Invalid/missing source facts can be retained as bounded text without fabricating a canonical row |
| `canonical_transaction` | `id UUID PK`, `owner_id`, `account_id`, `source_row_id`, `amount NUMERIC`, `direction TEXT`, `currency TEXT`, `posted_date DATE`, optional `transaction_date DATE`, optional `value_date DATE`, `created_at` | Composite account/source-row FKs enforce same owner and account. UNIQUE(owner_id,source_row_id); strict money checks above; direction debit/credit. Normalized facts are immutable. Classification does not change amount/date/source |
| `classification_event` | `id UUID PK`, `owner_id`, `transaction_id`, `revision INTEGER`, `category TEXT`, `review_status TEXT`, `actor_kind TEXT`, optional `actor_owner_id UUID`, optional `previous_event_id UUID`, optional `undo_of_event_id UUID`, optional bounded `reason TEXT`, `created_at` | Append-only classification and correction history; UNIQUE(owner_id,transaction_id,revision). Revision 0 = unknown/needs_review. Links to prior events must belong to the same owner and transaction. Actor synthetic_owner/system only; an owner actor must equal owner_id |
| `transaction_link` | `id UUID PK`, `owner_id`, `from_transaction_id`, `to_transaction_id`, `kind TEXT`, `created_at`, `actor_owner_id UUID`, bounded `reason TEXT`, optional `revoked_at`, optional `revocation_actor_owner_id`, optional `revocation_reason` | Explicit confirmed transfer/repayment/refund/reversal relation. Both transaction FKs include owner. Distinct endpoints, no reciprocal duplicate; uniqueness for active links. Preserve revoked links, timestamps and reasons instead of deleting evidence |
| `account_coverage` | `id UUID PK`, `owner_id`, `account_id`, `period_start DATE`, `period_end DATE`, `status TEXT`, `reconciliation_status TEXT`, `reason_codes TEXT[]`, `updated_at` | Composite owner/account FK; unique account/period, ordered finite dates. Status unknown/partial/complete; reconciliation unavailable/failed/passed. Missing record means unknown, never complete. No automatic complete default |

Text enums use named CHECK constraints rather than a free-form taxonomy. Categories: `unknown`, `income`, `consumption`, `internal_transfer`, `card_repayment`, `investment`, `refund`, `reversal`. Review statuses: `needs_review`, `confirmed`. A confirmed unknown is invalid. Amount/date extraction corrections beyond classification are later append-only normalization revisions; no arbitrary transaction UPDATE escape hatch is introduced today.

Every parent exposes the composite UNIQUE key required by its child FK: owner/id; additionally owner/account/id for sources and source rows, and owner/transaction/id for correction events. No single-column FK may bypass that scope. Index transactions by `(owner_id, posted_date, id)` and `(owner_id, account_id, posted_date, id)`; index source-row references, latest event lookup and both link endpoints. Unique constraints supply their matching lookup indexes; do not create redundant indexes. Check finite dates and bounded row/source keys. Composite keys and negative writes were verified directly against PostgreSQL 17.11; no SQLite substitution.

## Ownership and provenance contract

- A row for synthetic owner A cannot reference owner B's account, source row, correction event or link endpoint. Composite FKs enforce those relationships even when domain validation is bypassed. PostgreSQL [constraint guidance](https://www.postgresql.org/docs/17/ddl-constraints.html) supports composite foreign keys; cross-row semantic conditions need more than simple row CHECKs (accessed 2026-10-12).
- Foreign keys do **not** prevent unauthorized SELECTs. Owner-scoped repository methods must require trusted server context and include ownership in every query. A failed ownership lookup returns a generic unavailable result. Before public financial routes, Day 8 must authenticate and derive the owner independently of request input; review row-level security and database roles there. Do not mistake possession of an owner UUID for authorization.
- Keep the existing API health-only. No browser/account/transaction CRUD, no dashboard connection and no actual document collection. Synthetic test owners are not production users.
- Source identity is `(owner, account, source_key)` plus `(source, row_key)`, not amount/date/description. Same-amount genuine purchases remain separate. Replaying a source row with conflicting facts must reject, not overwrite or silently succeed. Parser version records provenance but must not make retries into fresh transactions. Overlapping different statements and probabilistic duplicate detection remain later import work.
- Use database mutation guards and application write restrictions for source snapshots, normalized facts and classification history. Privileged migration/purge roles remain capable of maintenance; immutable business history is not an indefinite-retention promise. Minimal logging contains opaque IDs and sanitized error codes, never source text, SQL parameter dumps or connection strings.
- Transaction correction appends an event; it does not edit original source facts. Serialize with a version update/lock on the owner row, require the expected latest revision, validate actor and category, then insert the next revision atomically. Concurrent stale corrections must fail safely. Current classification is the latest revision, avoiding a second mutable source of truth.
- Undo appends a new event restoring the state immediately before the latest correction and records `undo_of_event_id`; it does not delete an event. All subsequent classification changes conservatively revoke touching active relationships atomically, even if a fresh review could later confirm the same relation with actor/time/reason. Retries and history reads must remain owner-scoped.

## Deterministic reporting and relationship rules

Raw direction describes the statement movement; category describes the reviewed economic meaning; reporting treatment depends on account type, period, current review and confirmed links. A card credit is not automatically income. Reports enumerate included accounts and periods and disclose unknown activity.

| Activity | Income / consumption treatment | Cash-account movement and review |
| --- | --- | --- |
| Confirmed income credit | Add to observed receipt income; not taxable/gross income | Cash credit included once |
| Confirmed purchase debit, including card purchase | Add to consumption once | Bank/cash purchase affects cash flow; card purchase is liability activity, excluded from cash-account flow |
| Own-account transfer | No income or consumption | Both selected cash legs cancel; one included leg remains visible as a boundary movement. Unmatched candidate remains reviewable, never auto-matched |
| Card repayment | No income or consumption | Bank debit affects cash flow; card credit is settlement, not another cash inflow. Missing card history stays explicit |
| Investment contribution | Separate investment bucket; no ordinary spending | Cash debit included; redemption is not automatically income or capital gain and remains unresolved without supported treatment |
| Refund / reversal | Never ordinary income; confirmed consumption-linked credit reduces posting-period consumption | Preserve both original and return dates. Unmatched credit stays separate; no prior-month rewrite or inferred tax adjustment |
| Unknown credit/debit | Excluded from recognized income/consumption; reported by direction | Included in observed cash movement for cash accounts, with unresolved warning and qualified surplus withheld |

Implemented link validation: transfer = equal amount/currency, debit to credit, distinct owned cash accounts; repayment = bank/cash debit to card credit, equal amount/currency; refund/reversal = original debit to related credit with compatible reviewed meaning. Day 7 supports full-leg transfer/repayment pairing, not many-to-many allocation or fees disguised as matching tolerance. Multiple partial refunds may reference one original, each credit only once; sum of active confirmed refunds cannot exceed original consumption. Over-refunds, mismatched amounts and splits stay unresolved. Reversal is one equal opposite leg; do not also count it as a refund. Cross-row validation uses PostgreSQL triggers under the owner lock. Concurrent direct-SQL refund inserts, stale corrections and a correction racing a relationship update are tested. The version update also causes a serialization failure for stale snapshots at stronger isolation levels; automatic retries are not implemented. Callers roll back failed transactions and explicitly retry/review. Owner-level serialization trades throughput for a small, auditable implementation; later optimization needs evidence.

Reports use Decimal with an explicit sufficiently large context and traps for unintended inexact/rounded operations. The internal result retains Decimal values; any future API serialization must use decimal strings. Day 7 returns named deterministic buckets and coverage warnings for tests, not a new public analytics API. `observed_cash_movement` across provided cash accounts is not complete household net cash flow. Coverage requires explicit expected accounts/periods, reconciliation status and unresolved count; an empty account set is no-data. A caller asserting completeness is not independent evidence.

Executed fictional golden fixture: salary credit 1000.10; bank purchase debit 100.05; own transfer 200.00 debit/credit; card purchase 50.25; bank/card repayment 50.25 debit/credit; investment debit 100.00; linked purchase refund credit 20.00; unknown bank credit 3.60. Expected income **1000.10**, gross consumption **150.30**, refunds **20.00**, net consumption **130.30**, investments **100.00**, unknown credit **3.60**, selected-bank cash movement **773.40**. Card repayment/purchase are not counted twice. Qualified surplus is unavailable because the credit is unresolved. These independently derived expectations now pass against the repository and PostgreSQL fixture; no customer records were used. A January purchase refunded in February remains in January gross consumption; February shows its refund offset and cross-period reference under the proposed rule.

## Migration and repository implementation

- [Alembic configuration](../backend/alembic.ini), [environment](../backend/migrations/env.py), and revision template under `backend/migrations/`.
- Initial migration [0001_canonical_ledger.py](../backend/migrations/versions/0001_canonical_ledger.py) executes version-owned [0001_canonical_ledger.sql](../backend/migrations/versions/0001_canonical_ledger.sql). Later accepted schema changes must be new revisions, not edits to this SQL file.
- [Repository](../backend/app/ledger/repository.py) uses SQLAlchemy Core with psycopg and reflects the migrated tables. No second ORM schema or duplicated model metadata. The caller controls `engine.begin()` and commit/rollback boundaries; methods do not auto-commit.
- [Money validation](../backend/app/ledger/money.py) accepts Decimal/text, rejects floats/integers/bools/unsupported currencies and nonfinite/invalid amounts, and rejects precision loss. Reports use a local Decimal context sized for row count with loss traps.
- SQLAlchemy 2.0.54, Alembic 1.20.0 and their added dependencies are pinned. No frontend dependencies changed. Migration credentials come only from `DATABASE_URL`; no URL in alembic.ini, no echo logging, and SQLAlchemy parameters are hidden.

Run `python -m alembic upgrade head` from backend only against an explicitly selected synthetic database. No application-start migration, reset or production deployment was introduced. The automated test fixture proves a fresh upgrade and a repeated no-op upgrade. `downgrade()` deliberately raises before any destructive SQL; recovery is reviewed forward repair, preserving backups and revision state. No staging downgrade/reset/migration occurred.

### Concurrency, logging and security limitations

The `SyntheticOwner` object is an internal development contract, **not authentication**. Every repository read/mutation scopes by owner. SQL composite FKs independently reject cross-owner references. Direct database credentials can read other owners; RLS and authenticated server context are Day 8/security work. No public financial endpoints exist. Ordinary writer-role tests prove UPDATE/DELETE/TRUNCATE cannot rewrite source/history, while valid append/revoke operations work. Database owners/superusers can alter triggers; separate production migration/runtime roles and grants still need review.

`ledger_owner.write_version` serializes owner mutations and multi-query report snapshots. Corrections check expected revision and previous event, append audit context and revoke existing links in the same transaction. Undo does not silently restore links. Revocation preserves original relationship fields; reversal/refund duplicate-use and aggregate allocation checks execute in the database. Direct unsafe DML can encounter deadlock/serialization failures; failures must roll back, never be treated as success. Reports conservatively withhold the derived metric for missing accounts, failed/partial/conflicting coverage, unposted source rows, unknown activity or unmatched relationships. A cross-period relationship is disclosed without rewriting earlier periods.

Coverage is synthetic metadata here, not a built reconciliation engine or proof that users declared every account. Account archival, extraction corrections, full audit/purge workflows, report snapshots, automated import deduplication across different statements, many-to-many allocation and non-consumption reversals remain later work. Refund/reversal links currently require a consumption original. Runtime SQLAlchemy hides parameters and code does not log source content, but PostgreSQL default error DETAIL can contain failing rows. Test logs contain fictional data only; production database logging/error sanitization and retention must be hardened before any real records. Raw DBAPI errors must not be exposed by future APIs.

## Isolated PostgreSQL test safety and actual evidence

[compose.ledger-tests.yaml](../backend/compose.ledger-tests.yaml) creates a separately named `finnest-ledger-tests` project, private network, database `finnest_ledger_test` and migration owner `ledger_test_owner`. No host ports or staging volumes are attached. Its published password is **deliberately synthetic and test-only**, never suitable for deployment. Bootstrap stamps the database `DISPOSABLE_SYNTHETIC_DAY007` and creates a NOLOGIN writer test role.

The fixture requires `--ledger-postgres`, matching `TEST_DATABASE_URL`, approved host/database/user, no URL query overrides, `LEDGER_TEST_DATABASE_ACK=DISPOSABLE_SYNTHETIC_DAY007`, and the server-side database marker **before running migrations**. A pre-existing ledger schema is refused rather than reset. Guard tests reject ordinary staging database names, non-test users, external hosts, missing acknowledgement and query-host overrides. No test issues DROP DATABASE, TRUNCATE for cleanup, destructive downgrade or resets. Negative TRUNCATE tests run under the restricted role and fail as expected.

### Results — 2026-10-13

| Executed check | Result |
| --- | --- |
| Dedicated Compose runner, Python 3.13 / PostgreSQL 17.11 | **63 passed** in 9.16s, one existing Starlette/httpx deprecation warning |
| PostgreSQL-backed cases within that suite | **29 passed**: fresh/repeated upgrade, exact amounts and invalid direct SQL, ownership FKs/scoped access, immutable source/history, source identity conflicts and legitimate same values, undo/stale revisions, account/direction compatibility, transfers/repayments/investments, partial/cross-period refunds, coverage conflicts/unposted rows and concurrent correction/refund/link operations |
| Remaining cases within that suite | **21 money validation**, **8 database-target guards**, **5 existing health tests**, all passed; money validation remains exact even when the ambient Decimal context changes |
| `npm run lint`, `npm run typecheck`, `npm test`, `npm run build` | PASS in Linux Node 22.23.3; **5/5** existing exact frontend financial fixtures |
| `npm run test:browser` against production build | **31/31 PASS**: globe, four chapters, location mocks, financial corrections, keyboard/reduced motion and 320/390/768/1440px overflow |
| `python scripts/validate_manifest.py` | PASS: 194 feature IDs and 85 daily IDs unchanged |
| `python -m unittest discover -s tests -v` | **6/6 PASS** |
| `backend/.venv/Scripts/python.exe -m pip check` | PASS, no broken requirements |
| Documentation local-target check | PASS: 275 local targets, zero missing; external URLs and heading anchors are outside this check |
| `git diff --check` and new-file trailing-whitespace scan | PASS; Git's LF-to-CRLF notices are line-ending notices, not whitespace failures |
| Ordinary staging read-only probes | API readiness HTTP 200, frontend HTTP 200, PostgreSQL/API healthy; no tables in public/ledger schemas, no Day 7 migration applied |
| `python scripts/check_container_security.py` | PASS: rebuilt frontend/API images; 13 builder + 9 frontend runtime + 8 backend layers inspected with zero violations. All 24 synthetic environment sentinels removed; one existing environment file preserved unchanged. Frontend runtime user `node`, image 420,660,656 bytes. No ordinary service restarted |

Initial development run failed at migration setup because raw driver SQL interpreted PostgreSQL format `%I` as a psycopg placeholder. The migration now uses SQLAlchemy text compilation; the final fresh-database run passes. This was not a financial assertion failure and no staging data changed. A host-only early pytest run also emitted a Windows cache-directory permission warning; the final Linux run has only the pre-existing Starlette warning. Default `pytest` without `--ledger-postgres` explicitly skips the 29 database cases; it is **not** full ledger verification. The added CI job requires the dedicated suite, independent of the existing backend/frontend/container/tracker jobs. Remote execution of the new job awaits an approved push.

A final tracker rerun inside the restricted Windows sandbox could not create/clean its temporary directory (WinError 5). Re-running the identical command with approved filesystem access passed all six tests; no tracker or generated-file change was needed.

The container build emitted pip's standard root-install warning inside its isolated build stage; this does not imply a host installation or frontend runtime root user. Disposable ledger containers/network/database storage were removed after successful tests; the separate browser-test container was stopped. Ordinary staging remains running. Local evidence logs are ignored under `tmp/day07-ledger-final.log`, `tmp/day07-frontend-final.log`, `tmp/day07-browser-final.log`, `tmp/day07-container-security.log` and the existing container checker output `tmp/day06-container-security.json`; none is staged.

## Reproduce locally

From repository root, with Docker running:

```powershell
docker compose -p finnest-ledger-tests -f backend/compose.ledger-tests.yaml up --build --abort-on-container-exit --exit-code-from tests
```

This command intentionally fails if that test database already contains a ledger. To repeat, explicitly remove **only this disposable project** and then rerun; never run this against the ordinary staging configuration:

```powershell
docker compose -p finnest-ledger-tests -f backend/compose.ledger-tests.yaml down -v
```

The test command supplies its synthetic environment, performs fresh/repeated upgrades and all backend tests. The ordinary API stays health-only. For local non-DB checks use `backend/.venv/Scripts/python.exe -m pytest -q backend`; database cases will be labeled skipped. For a reviewed manual migration from backend, supply `DATABASE_URL` from the environment and run `python -m alembic current` / `python -m alembic upgrade head`. Never copy a real URL into docs or terminal output.

Existing checks from repository root:

```powershell
python scripts/validate_manifest.py
python -m unittest discover -s tests -v
python scripts/check_docs.py
docker compose config --quiet
docker compose ps
git diff --check
```

From frontend: `npm run lint`, `npm run typecheck`, `npm test`, `npm run build`; run `npm run start` and then `npm run test:browser` in another terminal. If staging owns 3000, use `npm run start -- --port 3003` with `APP_URL=http://127.0.0.1:3003/`. Tests use mocked location and fictional financial data. Stop the foreground server with Ctrl+C. No frontend source or financial route was changed by Day 7.

## Review, remaining decisions and Day 8

### Exact changed-file inventory

Six existing files modified:

- [.github/workflows/application.yml](../.github/workflows/application.yml)
- [backend/requirements.in](../backend/requirements.in)
- [backend/requirements.txt](../backend/requirements.txt)
- [docs/ARCHITECTURE.md](ARCHITECTURE.md)
- [docs/DECISIONS.md](DECISIONS.md)
- [docs/SECURITY.md](SECURITY.md)

Seventeen new files, including the Day 7 design document now completed as an implementation report:

- [backend/alembic.ini](../backend/alembic.ini)
- [backend/app/ledger/__init__.py](../backend/app/ledger/__init__.py)
- [backend/app/ledger/money.py](../backend/app/ledger/money.py)
- [backend/app/ledger/repository.py](../backend/app/ledger/repository.py)
- [backend/compose.ledger-tests.yaml](../backend/compose.ledger-tests.yaml)
- [backend/migrations/env.py](../backend/migrations/env.py)
- [backend/migrations/script.py.mako](../backend/migrations/script.py.mako)
- [backend/migrations/versions/0001_canonical_ledger.py](../backend/migrations/versions/0001_canonical_ledger.py)
- [backend/migrations/versions/0001_canonical_ledger.sql](../backend/migrations/versions/0001_canonical_ledger.sql)
- [backend/tests/Dockerfile](../backend/tests/Dockerfile)
- [backend/tests/__init__.py](../backend/tests/__init__.py)
- [backend/tests/bootstrap.sql](../backend/tests/bootstrap.sql)
- [backend/tests/conftest.py](../backend/tests/conftest.py)
- [backend/tests/test_database_safety.py](../backend/tests/test_database_safety.py)
- [backend/tests/test_ledger_postgres.py](../backend/tests/test_ledger_postgres.py)
- [backend/tests/test_money.py](../backend/tests/test_money.py)
- [docs/DAY_07_LEDGER.md](DAY_07_LEDGER.md)

No frontend, ordinary Compose, source manifest, generated tracker, branding, pricing or release-classification file changed. Ignored local environments, dependency/build output and synthetic test logs are not part of this inventory or a proposed commit.

O-04 requires **no further founder convention approval for this implementation**; amount ceiling is unchanged. Financial-professional, tax, legal, privacy and independent security reviews remain outstanding. Auth/provider choice O-07, retention O-06, production database roles/RLS, logging, encryption and deployment permissions remain release dependencies. Development dependency advisories from Day 6 are carried forward; they were not independently resolved by this backend work.

Proposed commit: `feat(DAY-007): add owner-scoped exact ledger and PostgreSQL migrations`. Proposed PR: DAY-007 canonical ledger foundation, referencing FIN-020/035/040/041/046/127 as incremental dependencies without marking them complete. Link the actual DAY-007 issue when independently confirmed; do not guess its number. Review the entire diff, require passing remote CI and obtain human acceptance before merge/verification. No commit, push, merge, issue closure or verified label was performed.

DAY-008 remains **Implement secure authentication and session recovery**. Its handoff is the tested owner-scoped repository, immutable provenance contract, migration revision and explicit synthetic-only context. Map verified identities to owner IDs on the server, deny client-selected ownership, add endpoint/session/recovery negative tests and review DB privilege/RLS separation before exposing financial APIs. The fictional dashboard remains disconnected. Do not treat this foundation as authorization to collect real customer data or as completion of Day 8.

# FINNest — security, privacy and trust requirements

**DAY-001 review draft · 2026-10-10. No controls below are claimed implemented or independently verified.** This is an engineering baseline, not a legal-compliance certification. See [requirements](REQUIREMENTS.md), [architecture](ARCHITECTURE.md) and [release gates](RELEASE_CHECKLIST.md).

## Real-data gate

No real customer financial documents may be collected before the necessary security, privacy and consent safeguards are implemented and verified. Development and discovery use synthetic or irreversibly anonymized material whose provenance and redaction have been checked. Do not ask interview participants to send statements. Anonymization is not a workaround for collecting raw customer files before this gate.

Before any real-data cohort, the owner must record approval backed by access-control tests, secure upload/storage and parser isolation evidence, purpose/consent notices, approved processors, export/deletion/retention behavior, verified recovery, monitoring and incident response, plus qualified privacy/legal and independent security review. No unresolved critical/high security findings. Research notes also require minimal collection and consent. No financial documents or sensitive identifiers in Git, issues, PRs, test output or support tickets.

## Implementation requirements

- **Identity and isolation:** verified identity, secure sessions, reset-token expiry, session revocation, abuse throttling and stronger authentication for privileged operations. Derive ownership from authenticated server context; enforce it on list/read/write/export/download/job/polling endpoints and worker outputs. Default deny. Never trust a client-supplied owner ID. Test owner A/B, CA A/B, expired/revoked sessions and privilege escalation.
- **Storage and encryption:** TLS, managed at-rest encryption for database/objects/backups, private buckets, scoped service identities, secrets manager and documented key rotation/recovery. No public object paths or credentials in source. Encryption does not substitute for authorization.
- **Upload safety:** quarantine before parsing; validate actual content and extension, file/page/size limits, malware checks and decompression/time/memory limits. Isolate parsers with minimal filesystem/network permissions. PDFs are untrusted content, including embedded instructions. Passwords are memory-only and excluded from queues, traces and logs; after worker failure ask again if required.
- **Consent:** present purpose, processor categories, retention and limitations before upload. Record notice version, timestamp and scope. Separate optional AI processing and CA sharing from core organization. Withdrawal blocks future processing for that purpose and triggers the applicable deletion workflow; disclose functions that then become unavailable. Do not silently bundle marketing consent.
- **Minimization and AI:** only approved minimal structured aggregates and opaque source references may leave the trusted boundary. Exclude full PDFs, raw narrations, PAN, account identifiers, credentials and unrelated transactions. Bind tool access to the authenticated owner independently of model input; no arbitrary SQL or document-database access. Review model-provider retention, training use, regions and subprocessors before enabling. Financial organization must remain usable if optional AI is declined.
- **Support access:** no standing access to raw documents or unrestricted impersonation. Begin with sanitized diagnostic IDs. Any exceptional content access needs a user-approved purpose, scoped time-limited grant, authorized operator and audit event; terminate on expiry/revocation. Prefer user-side correction or synthetic reproductions.
- **Audit:** log actor, action, opaque resource ID, scope, outcome, time and correlation ID for consent, access, edits, sharing, policy publishing and billing. Exclude source text, raw documents, amounts unless explicitly justified, tokens and secret URLs. Restrict log readers and protect integrity; detect unexplained access or missing events.
- **Payments:** hosted checkout, server-side order verification, authenticated/signed webhooks, replay defense, idempotent event persistence and explicit entitlement transitions. Secrets and raw card data do not enter application logs. Handle delayed, duplicate, failed and out-of-order events safely.
- **Operations:** isolated staging/production, dependency and secret scanning, monitored failed jobs/security events, retry limits/dead-letter handling, tested backups, restoration and rollback, and an incident owner with escalation contacts.

## Data lifecycle and retention

Exact durations and legal exceptions remain **pending owner and qualified legal approval** in [decisions](DECISIONS.md). No default indefinite retention; unresolved policies block real-data release.

| Data class | Required lifecycle | Evidence before real-data use |
| --- | --- | --- |
| Raw uploads, parsed rows and corrections | State purpose and retention; export originals plus normalized records/provenance; coordinated deletion across objects, database and derived reports | Inventory-to-deletion reconciliation, owner-only export tests, retention configuration |
| Quarantined/temp files and jobs | Short approved expiry; remove failed-processing remnants and ephemeral passwords; stop queued processing after withdrawal/deletion | Expiry/retry/crash tests and storage inspection |
| Reports, CA packages and AI caches | Versioned derivatives tied to source/owner; invalidate access and purge according to approved policy | Deletion propagation and stale-link tests |
| Backups | Bounded documented retention; no promise of immediate physical purge from immutable backups. Restrict access; expire on schedule; reapply deletion records before restored data becomes available | Restore drill demonstrating deleted accounts stay inaccessible; documented maximum residual period |
| Audit/security records | Separate minimum necessary retention and access restrictions; avoid retained document contents | Approved field inventory, retention schedule and access tests |
| Billing/legal records | Retain only justified fields for professionally confirmed obligations; explain exceptions to erasure and restrict further use | Legal rationale, duration, user notice and purge schedule |
| Third-party copies and interview notes | Processor-specific retention/deletion obligations; minimal notes and separate contact data; no raw financial evidence | Processor register/contracts and research consent/deletion process |

Account deletion must immediately disable sessions, shares and new jobs, then complete an auditable purge within an approved service window. Report pending steps and justified retained records; do not claim instant total erasure while backups or processors retain copies. Export generation and download must recheck identity/ownership and expire safely.

## CA permissions and revocation

The [DAY-003 workflow and sharing permissions matrix](research/DAY_03_CA_WORKFLOW.md) applies these requirements to proposed owner/recipient actions, including selected derived summaries, new package versions and clarification through an agreed external channel. It is a design draft, not evidence of access-control tests. FINNest does not protect an external communication channel; native messaging requires separate scope approval. CA discovery uses no client records and requires the [research consent process](research/DAY_03_CA_DISCOVERY.md).

Sharing requires explicit selection of documents/report snapshot, intended recipient identity, allowed actions (view/download), purpose and expiry. Do not grant all current/future documents or account browsing by default. Re-sharing and adding documents require new authorization; recipient must not widen permissions.

Check active scope on every new fetch through an authorization gateway. Long-lived direct object URLs must not bypass revocation. Test invitation forwarding, replay, changed ownership, cached links, expiry and concurrent revocation. Record access events for the owner.

Revocation blocks future authorized requests after the revocation is committed. It cannot retrieve downloaded copies, screenshots or bytes already delivered/in flight. Explain this before sharing; use cache controls and recipient obligations without promising technical recall. Deleting the FINNest account does not prove a CA deleted an independently retained copy.

## Risk register

Owners below are proposed accountable roles, not appointed reviewers. All risks are open; no mitigation has been verified.

| Risk | Impact / priority | Required mitigation and evidence | Proposed owner / follow-up gate |
| --- | --- | --- | --- |
| R-01 Cross-owner access or excessive CA scope | Critical confidentiality loss | Deny-by-default API/worker/storage checks; adversarial access matrix | Technical lead + independent security reviewer; before real data |
| R-02 Malicious uploads/parser escape | Critical compromise | Quarantine, scanner and resource/network isolation; malicious/oversized corpus | Technical lead; before imports with real data |
| R-03 Duplicate, misclassified or incomplete records | High misleading financial reports | Exact arithmetic, provenance, reconciliation warnings and independent golden fixtures | Technical lead + financial reviewer; before beta |
| R-04 AI leaks or invented figures | High privacy/trust harm | Minimal allowlisted tools, numerical trace checks, injection tests, vendor review | Technical lead + privacy reviewer; before AI enabled |
| R-05 Misleading tax readiness/policy | High user harm | Approved sources/applicability, qualified CA approval, no filing/liability promise | Appointed tax reviewer; before publication |
| R-06 Incomplete deletion or backup resurrection | High privacy harm | Full data inventory, retention schedule, processor purge and restore deletion tests | Owner + legal reviewer + technical lead; before real data |
| R-07 Shared download survives revocation | High expectation mismatch | Request-time enforcement and explicit downloaded-copy limitation | Technical lead + legal reviewer; before sharing |
| R-08 Payment/entitlement replay or refund errors | High loss/disputes | Signed webhooks, persisted event state, state-machine tests | Technical lead + owner; before paid rollout |
| R-09 Secrets/log/support exposure | High confidentiality loss | Minimal logs, secret scanning, restricted support grants and access audit | Technical lead; before real data and each release |
| R-10 Outage, data loss or failed restoration | High availability/integrity loss | Backup/restore and rollback drills; recovery budgets and incident contacts | Operational owner; before controlled beta |
| R-11 Unknown legal/processor obligations | High launch risk | Qualified applicability review, processor register and contracts | Product owner + external counsel; before real data |
| R-12 Schedule/reviewer/format uncertainty | High delivery risk | Book reviewers early, select formats from safe fixtures, reserve remediation time | Product owner; Days 2–5 and milestone reviews |
| R-13 Unvalidated value and upload willingness | High commercial risk | Genuine interviews, safe demonstrations, cohort value/cost measurement | Product owner; before scope/pricing commitments |

## External review questions

Qualified legal/privacy review must determine applicable Indian privacy obligations and effective dates, notice/consent and withdrawal requirements, breach reporting, rights handling, processor contracts, cross-border processing, age eligibility, retention exceptions and consumer/payment/refund obligations. These questions do not authorize data collection.

The official [MeitY DPDP Rules 2025 publication page](https://www.meity.gov.in/documents/act-and-policies/digital-personal-data-protection-rules-2025-gDOxUjMtQWa?pageTitle=Digit) is the starting reference for rules and enforcement material, not evidence of FINNest compliance. The [DAY-004 regulatory review](REGULATORY_REVIEW.md) records phased dates, CERT-In requirements and pending legal applicability checks. Its retention review must reconcile DPDP Rules 6/8(3), ICT logs, deletion and processor obligations before approving durations or public erasure promises. Recheck operative notifications with counsel at launch. Tax interpretation requires a qualified tax reviewer; independent security assessment must cover authorization, uploads, AI tools, sharing, billing and deployment. Review scope, dates, budget and reviewer identities are pending.

## Repository boundary

DAY-006's [foundation](DAY_06_FOUNDATION.md) exposes a synthetic frontend and operational API probes only. Optional rounded globe location stays in browser memory and can be cleared during a pending request; tests mock it. No financial upload/account/payment/tax/sharing routes exist. Compose binds frontend/API to loopback and publishes no database port; the ignored disposable local password is not a production secret. Health failures return sanitized status, and public API documentation is disabled. These limited measures do not satisfy the real-data gate, isolation, authentication or independent-review requirements above. Development lint dependencies have unresolved audit findings recorded in the foundation report; public release is not approved.

Preserve private development settings where configured; do not infer remote visibility. Do not run unreviewed PR code with write credentials. Stable identifiers, generated-document ownership and human acceptance rules are documented in [GitHub automation](GITHUB_AUTOMATION.md). No tracking percentage proves security readiness.

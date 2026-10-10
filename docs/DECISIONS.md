# Architecture and product decision log

## Existing decisions

| Date | Decision | Rationale | Review trigger |
| --- | --- | --- | --- |
| 2026-10-09 | Working brand FINNest, not legal final | Rebrand without changing stable IDs | Trademark review or pivot |
| 2026-10-09 | Web first, modular monolith | Best for solo developer + Astra | Scale evidence |
| 2026-10-09 | CSV/PDF uploads before bank API | Avoid premature regulated integrations | Bank-sync willingness to pay |
| 2026-10-09 | AI explains calculated facts | Financial arithmetic reliability | New approved analytics capabilities |
| 2026-10-09 | Tax readiness only in V1 | Expert verification required for tax liability calculator | V2 tax review |
| 2026-10-09 | GitHub verified issue -> auto checked | Closed task is not proof of accuracy | Team review policy |

## Owner-approved Day 1 amendments — 2026-10-10

Approval sources: the owner's “Day 1: Approved with Amendments” and subsequent “Day 1 Final Reconciliation” instructions for [DAY-001 / Issue #1](https://github.com/Tejanshu22/PersonalFinanceManager/issues/1). The later approval authorizes the four manifest deferrals and local regeneration. It does not authorize final verification, application implementation or GitHub writes.

| ID | Approved decision | Impact |
| --- | --- | --- |
| D-01 | Defer FIN-027, FIN-063, FIN-066 and FIN-067 to V1.5, preserving IDs | Reconciled V1 count 140 / V1.5 count 14 under D-07; no IDs renumbered |
| D-02 | Supported CSV mappings, one Indian bank PDF format and one card format, corrections/deduplication/reconciliation; unsupported formats fail gracefully | Provider/version selection pending safe fixtures; no arbitrary choice or scanned-PDF promise |
| D-03 | Maintain 85-working-day target: Day 60 internal functional beta; Day 75 security-reviewed release candidate; Days 76–80 gated real-user beta; Day 85 target public launch | Targets are conditional; exact roadmap edits remain separately approvable |
| D-04 | Move privacy, financial access controls, fixtures and security infrastructure earlier in the dependency plan | No real customer documents before necessary safeguards are implemented and verified |
| D-05 | Document tracking follow-ups; preserve scripts, configuration, generated files and master | Initial drafting preserved those files; D-07 subsequently authorizes feature-manifest changes and generated output only |
| D-06 | Define the individual paying customer and Upload → Reconcile → Correct → Understand → Prepare Tax Documents → Share with CA → Upgrade journey | Pricing and demand remain hypotheses; genuine interviews required |
| D-07 | Final source reconciliation explicitly authorized by the owner | Change only release V1 → V1.5 and target_day → null for the four deferred IDs; preserve titles, acceptance, priorities, owners, remaining releases and the daily roadmap. Regenerate locally without commits/pushes or issue mutations |

## Unresolved decisions — separate from approvals

Proposed owners are roles to appoint, not completed assignments. All items below are pending.

| ID | Decision needed | Proposed owner / timing | Draft recommendation or dependency |
| --- | --- | --- | --- |
| O-01 | Accept the full Day 1 requirements and 14-journey thresholds | Product owner; DAY-001 review | Review financial definitions, corpus minimums and performance/recovery targets; no results implied |
| O-02 | Approve concrete day-to-feature mapping and roadmap wording | Product owner; subsequent scoped change | Feature deferrals are reconciled under D-07; day allocation, milestone wording and any priority changes remain pending |
| O-03 | Select bank/card format versions and support limits | Product owner + technical lead; after safe fixtures | Consider actual interview needs and fixture coverage; no provider chosen |
| O-04 | Approve INR-only initial boundary, posted-date reporting, cross-period refund treatment, savings label and rounding/precision | Product owner + financial reviewer; before schema/analytics | Draft semantics are in REQUIREMENTS; unresolved legal/tax questions go to qualified reviewer |
| O-05 | Appoint tax, privacy/legal and independent security reviewers, budget and review slots | Product owner; begin Days 2–5 | External review and remediation must precede corresponding release gates |
| O-06 | Approve retention/purge durations, backup window, research-note policy and justified legal exceptions | Owner + legal/privacy reviewer; before collection | No indefinite default; demonstrate restore cannot resurrect deleted access |
| O-07 | Approve auth/hosting/storage/model/payment providers, regions and spending limits | Owner + technical lead + privacy reviewer; before integrations | Processor terms and merchant approval are dependencies |
| O-08 | Approve free quotas, Plus/Tax Pack overlap, purchase period/window, renewal, refunds and post-expiry access | Product owner + legal reviewer; before billing | Validate prices; preserve proposed privacy/export/correction trust floor |
| O-09 | Agree CA view/download scopes, recipient proof, expiry limits and support exceptional-access process | Owner + security/legal reviewers; before sharing/support | Explain inability to recall downloaded copies |
| O-10 | Approve classifier confidence policy, recurring/AI eval rubric, corpus and load/recovery budgets | Owner + technical/financial reviewers; before implementation acceptance | Thresholds in REQUIREMENTS are proposals, not calibrated guarantees |
| O-11 | Resolve brand/domain/legal-entity clearance | Product owner + qualified adviser; before public marketing | Keep configurable FINNest and existing repository name |
| O-12 | Confirm remote issue body/labels, CI/rulesets/default branch and verification permissions | Repository owner; when read access works | Local evidence supports master workflows; remote state remains unverified |

## Roadmap and catalog consistency assessment

Inspection found 194 features, 85 sequential daily IDs and matching catalog/CSV identities. All 279 owners remain “Unassigned”; all 85 daily acceptance fields use the same generic sentence. These are structural validity findings, not evidence of implementation.

| Finding | Proposed follow-up / impact |
| --- | --- |
| Manifest/catalog now show 140 V1 and 14 V1.5 | Four approved deferrals reconciled; generated status remains the explicitly cached snapshot, not fresh remote evidence |
| FIN-001–008 all target Day 1; interviews/research/landing page occur Days 2–5 | Map actual feature acceptance to days; Day 1 cannot claim interviews or a built landing page |
| Retained V1 FIN-017–034 entries still target Day 14; PDFs are Days 21–25, while Day 26 still schedules deferred FIN-027 | Proposal: retain DAY-026 but replace second-adapter work with first-bank/card format regression and privacy/recovery work; define exact acceptance before approval. No Day 26 edit made |
| Day 40 still schedules health components, now deferred FIN-066 | Proposal: retain DAY-040 for monthly-report/coverage/financial-fixture hardening; exact task/acceptance awaits O-02 |
| FIN-063 and FIN-067 have no dedicated daily task or explicit dependency edge | Do not infer free days or remove other recurring/report work; review Days 36–40 and future notification dependencies during O-02 |
| AI features target Day 43 but evaluation is Day 45; CA features target Day 57 but access tests run through Day 59 | Acceptance dates must include test/review work, not only interface delivery |
| Billing features target Day 62; failure/refund/UI tests continue through Day 65 | Update completion expectations without claiming earlier acceptance |
| Security features are broadly P1/Day 69 and infrastructure P1/Day 74 | Treat prerequisite security/CI/fixtures as early release blockers; exact priority/date edits pending |
| Generated Day 60 still says feature freeze; billing/privacy come later | Keep Day 60 as internal functional beta. Proposal: rename DAY-060 to “Internal functional beta integration review” and define safe-fixture evidence; do not imply public V1 feature completeness. Wording change waits for O-02 |
| Consent/deletion currently Days 66–67; security assessment Day 75 | Bring prerequisite implementation forward, book review early and reserve remediation capacity |
| Only limited beta feedback/remediation time remains before Day 85 | 85 days is 17 five-day weeks at the existing 6–8-hour/day assumption, not a guarantee; reviewer delays or failed gates move launch |
| No explicit dependency graph or per-day evidence definitions | Author a minimal feature/day mapping and specific acceptance, preserving 85 IDs; do not infer progress from target dates |

The daily manifest retains all 85 IDs/tasks. Day 85 already says limited public launch only if security/accuracy gates pass and is unchanged. Deferred features are not prerequisites for the retained ledger, monthly report, recurring candidates, AI, tax readiness or CA sharing; no machine-readable dependency graph exists to prove broader scheduling feasibility. The [architecture dependency plan](ARCHITECTURE.md) proposes ordering only. Four deferrals do not establish that 140 acceptance items fit the schedule. No reliable effort estimate exists until formats, reviewers, fixture work and provider constraints are known.

The local generated tracker maps DAY-001 to #1, FIN-001–008 to #2–9 and DAY-002–004 to #10–12; other manifest items lack issue links in the inspected snapshot. Partial issue creation is intentional, not missing IDs. Live GitHub reads during inspection failed with network/TLS errors; no remote issue status, latest body, CI or protection settings are asserted.

## Engineering follow-ups — not implemented or filed as new issues

These local reference IDs are discussion items, not new FIN/DAY identifiers or GitHub issues. Obtain separate implementation approval and map them to an existing/new approved issue.

| Ref | Required follow-up | Acceptance evidence |
| --- | --- | --- |
| T-01 | Represent open issues awaiting review as Needs Review; define label/status precedence | Tests for submitted/open, blocked, reopened, canceled and closed/verified states |
| T-02 | Validate inputs before artifact generation and bot commits | Invalid schema/IDs/duplicate issue mappings fail before changing generated output |
| T-03 | Prevent accidental overwrite by one-time build_manifest/build_daily_plan seed helpers | Explicit guarded authoring/reset behavior; existing authored changes cannot be overwritten silently |
| T-04 | Require human acceptance and evidence before verified label/closure | Merged PR, passing CI, reviewed acceptance, relevant security/privacy/financial/tax checks and updated docs linked in issue |
| T-05 | Confirm master compatibility and repository protection/permission behavior | Read-only remote settings/CI inspection; any workflow change separately reviewed |
| T-06 | Preserve stable IDs and generated ownership | Regression checks and documented source-to-generated flow; no manual progress edits |
| T-07 | Improve tracker CI coverage and dependency reproducibility | Define checks for validator, status precedence and workbook generation; review dependency lock/pinning in a separate change |
| T-08 | Agree how generated Markdown hard breaks and CSV CRLF are checked for whitespace | Current raw git diff --check flags five generated-format lines after regeneration; authored changes pass. Review a targeted formatting/check policy or generator fix separately, without manual generated-file edits |

Current tracker computes closed + verified, excluding canceled/wontfix; it does not inspect reviewer approvals, merged PRs or CI. An open issue awaiting review currently has no Needs Review mapping. Human verification is a required process gate, not currently machine-enforced evidence validation.

## Day 1 evidence boundary

Documentation changes must be reviewed before final acceptance. Only repository/documentation/tracker checks can run now; there is no application, financial fixture suite, product lint/type pipeline or completed customer research to validate. Test results are recorded in [DAY_01_KICKOFF](DAY_01_KICKOFF.md). No commit, push, merge, issue closure or verified label is authorized by this draft.

The final reconciliation verifies that the required Day 1 documentation is present and the four deferrals are represented in the source manifest and generated views. It does not resolve open pricing, financial-policy, reviewer, retention or roadmap choices. Final owner acceptance, merged PR/CI evidence under AGENTS.md and explicit authorization to verify/close Issue #1 remain outstanding. Live GitHub reads still time out; local regeneration is based on the preserved cached snapshot. Existing ExcelJS transitive dependency deprecation warnings were observed during the normal renderer dependency install; no dependency upgrade or security-audit result is claimed (T-07).

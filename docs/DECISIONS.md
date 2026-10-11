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

## DAY-002 research preparation — Issue #10

The owner authorized preparation for five distinct real interviews, approximately 15–20 minutes each, with actual findings to be supplied later. The [guide](DAY_02_INTERVIEW_GUIDE.md), [five participant templates](DAY_02_INTERVIEW_NOTES.md) and [assumption/evidence register](DAY_02_RESEARCH_SUMMARY.md) are prepared instruments, not completed research. The guide replaces Day 1's longer preparatory outline. No source manifest, architecture or feature priority changes are authorized by research preparation.

The working tree was clean on master at the start of this task. The local generated roadmap now displays DAY-001 as Verified Done and DAY-002 as Planned; the historical Day 1 evidence text above describes its earlier snapshot. No conclusion about Day 2 interview completion follows from that display. A read-only request for Issue #10 timed out, so the latest remote body/labels and any additional acceptance instructions remain unconfirmed. No issue or label was changed, including in-progress.

Research references below are local decision notes, not new FIN/DAY IDs or GitHub issues. All remain pending unless explicitly stated; no customer evidence has resolved them.

| Ref | Arrangement or decision needed | Owner / when | Preparation default or boundary |
| --- | --- | --- | --- |
| D2-01 | Identify interviewer/recruiter, five distinct willing participants and session times | Product owner; before interviews | Seek relevant responsibilities, varied workarounds and skeptics; no actual people or recruitment assumed |
| D2-02 | Choose private research storage, access, retention/deletion period and withdrawal channel | Product owner; before collecting notes | No identifying records in Git; participant codes alone do not prove anonymity; do not collect notes while these arrangements are unspecified |
| D2-03 | Agree permission wording for notes, repository excerpts, quotations and assistant analysis | Product owner; before respective uses | Separate participation from sharing/AI permission; recordings off by default; no raw recordings/transcripts in repository |
| D2-04 | Decide whether any recruitment incentive is needed | Product owner; only if proposed | None assumed; any incentive must not depend on positive product feedback |
| D2-05 | Review five-interview evidence and summary against DAY-002 acceptance | Product owner; after actual responses | Material coverage, privacy, dissent and evidence traceability matter; positive opinions are not required for completion |
| D2-06 | Select Day 3 follow-ups based on genuine evidence and sampling gaps | Product owner; after Day 2 notes | Existing plan is five more prospects and two CAs; no new interviews or reviewer appointments invented |

Existing unresolved product decisions O-03/O-08 and trust assumptions can be informed by this research; interviews do not replace O-05 professional review or prove production controls. Findings may recommend feature-priority changes only after real responses and owner review. The 140-item V1 scope and four V1.5 deferrals remain unchanged.

## DAY-002 preliminary survey integration — 2026-10-11

The owner authorized adding the supplied [anonymized pilot report](research/DAY_02_SURVEY_PILOT.md) and updating research documentation. This authorization covers documentation only. The source summarizes five actual Google Form submissions: two salaried employees, one salary-plus-freelance respondent and two students. Analyze the three employed respondents separately; the students' feedback is auxiliary. Underlying raw rows and consent records were not independently inspected, and no raw export, identity, recording or financial record was copied into the repository.

The [evidence register](DAY_02_RESEARCH_SUMMARY.md) attributes aggregate signals using SP-01–SP-09 and separates them from researcher interpretation. The earlier preparation-only descriptions above are historical: preliminary survey evidence now exists, but documented usable interviews remain **0/5**. No survey respondent is assigned to P01–P05. Five submissions do not satisfy DAY-002's five real interviews or FIN-002's wider ten-interview criterion. No label or issue state is changed by this integration.

| Ref | Evidence-informed question / proposal | Decision status and next evidence |
| --- | --- | --- |
| D2-07 | All 3 employed respondents selected confusing descriptions/transfers, tax-reporting uncertainty and recurring-upload effort | Research follow-ups recorded, not validated severity or approved priority changes. Obtain recent incidents, workarounds, consequences and cadence; retain reports of no recent difficulty and straightforward filing |
| D2-08 | Access visibility, independent assessment and CA revocation may influence trust | Test comprehension and refusal conditions; selected safeguards do not prove an audit exists or permit real-document collection. D2-02/D2-03 and O-05 professional-review arrangements remain pending |
| D2-09 | Annual-price bands split across employed respondents; one unspecified respondent's paid-service answer is contradictory | Existing prices/entitlements unchanged. Clarify actual past purchases; do not infer clean nonpayment, conversion or Tax Pack demand from annual bands |
| D2-10 | CAND-D2-01: one student's budget-threshold alerts/adaptive-budget suggestion | Unvalidated candidate for discussion only; related FIN-147 remains V1.5 with unchanged acceptance. No new FIN ID or release assigned; require employed-user behavior evidence and explicit owner approval before backlog changes |
| D2-11 | Report suggests collecting 15–25 varied survey responses and ideally CA input alongside interviews | Optional expansion pending owner capacity decision; no new acceptance gate. Existing five target-customer interviews remain required; CA consultation cannot replace one. Day 3 retains its planned five additional prospects and two CAs |

Report priority labels and requests to link evidence on GitHub are source recommendations, not instructions executed here. There is no authorization to change releases, pricing, architecture, source manifests or generated tracking, begin Day 3, conduct outreach, collect statements, commit or push. D2-01–D2-06 remain open; the pilot does not appoint interviewers/reviewers, establish privacy arrangements or approve completion. Final synthesis waits for actual anonymized interview notes and owner review.

## DAY-002 acceptance amendment — founder approved, 2026-10-11

The founder explicitly approved replacing the original five completed Day 2 interviews with a limited exploratory pilot based on five genuine Google Form submissions, to avoid delaying development. This supersedes the Day 2 interview gate in the earlier preparation/pilot entries and D2-05; it is not evidence that interviews occurred. See [closeout criteria](research/DAY_02_CLOSEOUT.md), [survey report](research/DAY_02_SURVEY_PILOT.md) and [evidence register](DAY_02_RESEARCH_SUMMARY.md).

Revised acceptance: anonymized aggregate analysis; separate three employed respondents from two students; limitations and financial clarity, transaction confusion, privacy, tax-readiness and upload-friction findings recorded; V1/pricing preserved; new nonblocking issue for five future interviews; revised criteria/evidence on Issue #10; actual validation results; final human acceptance and confirmed publication before verification. Scope approval is recorded now; final acceptance, commit/push and closure are not yet approved or performed.

FIN-002 retains its at-least-ten-real-interviews acceptance and remains open/unverified. The new follow-up contributes five actual interviews without duplicating the FIN-002 tracker ID. D2-01–D2-04 research arrangements remain pending for that future work; they are not survey-closeout prerequisites. D2-06 becomes the Day 3 handoff: proceed with CA workflow discovery and other planned research without waiting for the deferred interviews. No daily manifest is rewritten; its interview-oriented DAY-002 task text is historical planning context, superseded for milestone acceptance by this decision and Issue #10. Future interview timing should be before final V1 feature freeze or broad real-data onboarding; existing security/privacy release gates remain in force.

The five-response convenience sample supports hypotheses, not demand, conversion, statistical prevalence, audited security or tax-professional review. Prices and approved V1 features are unchanged; CAND-D2-01 budget alerts remains unvalidated. No raw exports, identities or recordings are added. The user authorized Issue #10 edits and creation of the follow-up now, but requires a further confirmation before committing or pushing to master. AGENTS.md verification evidence is still required before a verified label/closure; attached instructions are not a waiver.

Remote follow-through is pending: API TLS timeouts and a signed-out browser prevented Issue #10 edits and follow-up creation. The browser confirmed DAY-002 #10 and FIN-002 #3 are open. Ready-to-post drafts and current evidence status are retained in the closeout document; no new issue ID or successful remote update is claimed. DAY-003 #11 still has its existing five-prospect/two-CA task; this Day 2 amendment does not waive Day 3 acceptance.

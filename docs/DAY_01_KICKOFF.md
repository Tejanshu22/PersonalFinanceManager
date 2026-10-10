# FINNest — DAY-001 product foundation review

**Repository:** [Tejanshu22/PersonalFinanceManager](https://github.com/Tejanshu22/PersonalFinanceManager)

**Issue:** [#1 — DAY-001](https://github.com/Tejanshu22/PersonalFinanceManager/issues/1)

**Date:** 2026-10-10

**Status:** Documentation draft awaiting owner review; DAY-001 is not complete or verified.

The owner approved drafting with four feature deferrals, one bank/one card format and conditional 85-day milestones. This approval does not mean the full requirements, pricing or proposed acceptance thresholds have been accepted. No application implementation, manifest reconciliation, tracking-script change or GitHub write is part of this pass.

## Review packet and deliverables

| Deliverable | Existing document | Review focus |
| --- | --- | --- |
| Product requirements, personas and all-feature release disposition | [REQUIREMENTS](REQUIREMENTS.md) | Primary/secondary/future B2B hypotheses; clear V1 limits; unchanged IDs |
| Financial semantics and 14 measurable journeys | [REQUIREMENTS](REQUIREMENTS.md) | Income/spending/cash-flow distinctions, coverage, evidence and proposed thresholds |
| Business model and validation | [MONETIZATION](MONETIZATION.md) | Buyer/value journey, prices, costs, conversion/retention definitions and open entitlements |
| Security/privacy risk register | [SECURITY](SECURITY.md) | Controls, data lifecycle, CA limitations, proposed owners and legal/security dependencies |
| Tax source and review governance | [TAX_POLICY](TAX_POLICY.md) | Historical/current periods, qualified approval and rollback |
| Dependencies and architecture | [ARCHITECTURE](ARCHITECTURE.md) | Secure ordering before real data; no implementation claims |
| Roadmap findings, approvals and unresolved choices | [DECISIONS](DECISIONS.md) | Approved scope versus unchanged manifests; follow-up tasks |
| Release gates | [RELEASE_CHECKLIST](RELEASE_CHECKLIST.md) | Real-data, release-candidate, controlled-beta and public-launch evidence |
| Day 2 preparation | This document | Actual recruitment, consent, script and evidence template |

The authoritative [feature](../data/features.json) and [daily](../data/daily_plan.json) manifests remain unchanged. They still show 144 V1 items and the original day schedule; the approved documentation proposal is 140 V1 items. Generated catalog, roadmap, progress, completion log and sheets must not be hand-edited. Reconciliation requires a separately approved change.

## DAY-001 acceptance checklist — owner review pending

- [ ] Primary and secondary personas, future CA persona and excluded users reviewed.
- [ ] Explicit V1 scope, four deferrals and regulated exclusions reviewed.
- [ ] Pricing/business hypotheses and genuine interview plan reviewed.
- [ ] Financial accuracy definitions and incomplete-data treatment accepted.
- [ ] Security/privacy risks and external review dependencies accepted.
- [ ] All 14 acceptance journeys, proposed thresholds, evidence and dependencies reviewed.
- [ ] Roadmap findings and separately approvable changes acknowledged.
- [ ] Open decisions and Day 2 readiness reviewed.
- [ ] Documentation diff and available test results reviewed.
- [ ] Approved PR references DAY-001 and Issue #1, is merged with passing CI, and required human acceptance is recorded.
- [ ] Owner explicitly authorizes verified label and issue closure after the completion gate.

All boxes remain unchecked in this draft. The owner, not an AI-generated document or passing tracker test, approves acceptance.

## Day 2 interview preparation

**Target:** five genuine salaried prospects on Day 2; five additional prospects and two CAs on Day 3, consistent with FIN-002/003. Recruitment and interviews have not occurred. Aim to include both target individual personas across the ten, varied account/card usage and people skeptical of uploads. This is qualitative discovery, not a representative market survey.

Use 30–40 minutes per prospect. The product owner recruits and conducts interviews; Astra may help structure anonymized notes but must not substitute invented participants or answers. Anonymized IDs P01–P10 and CA01–CA02 are research references, not product accounts. Store contact details separately from notes with approved access/retention; do not place identifying interview records in Git.

### Before each interview

- Explain that this is research about an unbuilt product, with no promise of tax advice, financial outcomes or launch date.
- Ask permission for minimal notes; recording is optional and requires separate consent. Allow skipping questions or stopping. Explain how to request removal and disclose any approved retention exceptions.
- Do not request statements, account numbers, PAN, payslips, passwords, tax documents, salary amounts or client records. No collection of real customer financial documents before the verified safeguards gate.
- Use clearly labeled synthetic report examples only. Do not imply a static example was produced by working software.
- Ask provider/format names only if the participant is comfortable; no document upload. Fixture sourcing later requires permission, safe handling and irreversible anonymization review.

### Suggested conversation

1. **Past behavior (8 minutes):** “Tell me about the last time you reviewed spending or gathered documents for a CA.” What tools, steps, difficulties and repeated work were involved? Avoid asking whether the proposed product is “a good idea.”
2. **Current trust and refusal (6 minutes):** “What would stop you uploading a statement to a new service?” Ask about deletion, sharing, AI, security evidence and acceptable alternatives. Record a refusal as useful evidence.
3. **Synthetic value exercise (8 minutes):** Show a labeled example containing a card purchase, repayment, own-account transfer and missing statement period. Ask the participant to explain spending, cash flow and the warning. Observe confusion without coaching, then explain.
4. **Workflow burden (5 minutes):** Ask how they obtain CSV/PDF files, whether monthly uploading and correction are acceptable, and what their current workaround does better.
5. **Pricing tradeoff (5 minutes):** Only after value/limits are clear, present free, ₹999/year Plus, ₹499 Tax Pack and “neither.” Ask what they would choose, what they would give up, and whether a reporting-period pack or inclusion with Plus is clearer. No purchase or commitment required.
6. **Return and next step (3 minutes):** “What event would bring you back next month?” Ask separately for consent to a future research invitation. Do not treat that consent as upload or marketing consent.

For CA interviews, focus on required document coverage, period labels, source traceability, missing-information questions, access/revocation expectations and whether the synthetic package supports a real review task. Do not solicit client documents. Discuss professional-review availability separately from product endorsement.

### Evidence template (empty until genuine research)

| Field | Record |
| --- | --- |
| Participant ID / date / segment | Non-identifying ID and declared segment |
| Research consent / withdrawal channel | Approved notice and scope; no contact details in repository |
| Recent workflow and tools | Participant report; distinguish observation from recollection |
| Pain and workaround | Concrete example without sensitive financial content |
| Upload willingness / refusal | Conditions, objections and any changed answer after explanation |
| Synthetic exercise | Task attempted, observed understanding/errors, help required |
| Pricing response | Choice including neither, rationale and alternative; hypothetical only |
| Return/use hypothesis | Stated trigger; not measured retention |
| Evidence type | Observation / participant claim / facilitator inference |
| Follow-up and uncertainty | Contradictions, missing evidence and next question |

No rows are prefilled with invented findings. Record denominator and number of interviews actually completed; missing participants stay missing. Summarize disconfirming evidence and differences between personas before proposing changes.

### Day 2 readiness checklist

- [ ] Five actual prospects recruited with voluntary participation.
- [ ] Research notice, minimal-note storage/access and retention/withdrawal process agreed.
- [ ] Synthetic examples prepared and clearly labeled; no customer uploads.
- [ ] Interviewer, schedule, script and unfilled evidence template ready.
- [ ] Day 3 recruitment for five more prospects and two CAs begun.
- [ ] Reviewer availability/budget questions prepared without claiming appointments.
- [ ] Owner agrees how findings will inform format selection, packaging and scope.

## Validation record

Executed on 2026-10-10 against this documentation draft:

| Check | Observed result | Limit |
| --- | --- | --- |
| python scripts/validate_manifest.py | PASS: 194 features, 85 working days | Validates existing manifest structure, not schedule realism or product behavior |
| python -m unittest discover -s tests -v | PASS: 6 tests, 0 failures/errors | Existing tracker suite; approved execution outside sandbox used because inspection had exposed a Windows temporary-directory restriction |
| Read-only documentation audit | PASS: local Markdown targets resolve and are relative; changed files have balanced code fences and no replacement characters | Custom inspection, not a repository-provided Markdown linter |
| Feature/journey audit | PASS: all 194 feature IDs covered exactly once in release-disposition table; 14 numbered acceptance journeys present; 144 current / 140 proposed V1 arithmetic matches | Checks coverage, not correctness of future implementation |
| Protected-file diff | PASS: manifests, generated artifacts, scripts, tests, workflows, tools and configuration unchanged from HEAD | Documentation-only scope check |
| git diff --check | PASS after removing three trailing-space lines | Whitespace validation, not a product test |

The initial whitespace check found three Markdown hard-break lines with trailing spaces; these were removed before final validation. No application, financial fixture suite or product lint/type pipeline exists yet; none was invented or claimed run. No independent security assessment or customer research has been completed by this documentation work. No product capability is verified by these checks.

# FINNest — Day 1 kickoff

**Repository:** https://github.com/Tejanshu22/PersonalFinanceManager  
**Goal:** establish a frozen, testable V1 product definition and development success criteria, without falsely claiming any app code is finished.

## Outputs to make today

1. Review `docs/REQUIREMENTS.md` and `docs/FEATURE_CATALOG.md` with Astra, especially V1 versus later features.
2. Confirm the target persona: Indian salaried professionals with multiple accounts and occasional non-salary/investment income; list exclusions.
3. Lock the V1 buyer value proposition: reliable user-uploaded statement analysis, clear cash-flow insights, tax-document readiness, and secure basic CA sharing.
4. Check that no first-release requirement silently assumes unrestricted bank-account APIs, automatic ITR filing or autonomous tax-law decisions.
5. Define measurable acceptance criteria and release gates: source reconciliations, cross-account data isolation, privacy/security review, reproducible financial calculations and informed user consent.
6. Record priorities and open product decisions in `docs/DECISIONS.md` and adjust `docs/REQUIREMENTS.md` only where needed.
7. Review branding as a working name (`config/brand.json`) and record trademark/domain due diligence as pending.
8. Use the GitHub Issue `[DAY-001]` to capture evidence and links to changed docs; do **not** apply `verified` until a human has checked all acceptance points.

## Suggested acceptance checklist for DAY-001

- [ ] Target user and excluded users are explicit
- [ ] V1 capabilities and out-of-scope integrations are explicit
- [ ] Key accuracy, privacy, security and tax-review risks documented
- [ ] Payment/value assumptions phrased as hypotheses, not guarantees
- [ ] User interview targets and open questions recorded for Days 2–3
- [ ] Documentation committed to GitHub with references in the issue
- [ ] Human reviewer has examined the changed documents

## Copy into Astra as your first instruction

> Read `AGENTS.md`, `docs/REQUIREMENTS.md`, `docs/SECURITY.md`, `docs/TAX_POLICY.md`, `docs/MONETIZATION.md`, and `data/features.json` before making any changes. We are starting FINNest Day 1, working from GitHub issue `[DAY-001]`. Do not implement application code. Audit the V1 product scope and produce a concise list of inconsistencies, missing acceptance criteria, implicit banking/tax/API dependencies, privacy risks and overly optimistic claims. Suggest only minimal documentation edits. Explain which documents you would update, request approval for any material scope change, and keep Day 1 marked as unverified until a human reviews the results.

## Next day

Day 2 is five genuine prospective-user interviews. Do not substitute AI-generated mock interviews for real customer feedback. An Astra-generated interview questionnaire is appropriate; evidence of user demand must come from actual people.

# FINNest — release gates and evidence

**DAY-001 review draft · 2026-10-10. All gates below are pending.** This manually reviewed checklist is not a claim of implementation. Generated percentages cannot authorize release.

## Evidence standard

For each applicable gate record build/commit, environment, versioned synthetic/anonymized fixtures, expected and actual results, unresolved defects, reviewer identity/date and approval scope. Store only privacy-safe evidence in the repository or issues. A passing tracker test does not validate financial code or production security.

The [14-journey acceptance matrix](REQUIREMENTS.md) defines proposed functional thresholds. Reviewer acceptance of those thresholds is pending. Any revised threshold must be explicitly approved before testing, not lowered retroactively to turn a failure into a pass.

## Before collecting any real customer financial document

- [ ] Owner approves the specific cohort and purposes after reviewing all required evidence.
- [ ] Authentication, ownership and CA scope checks pass negative tests across APIs, objects, exports, jobs and caches.
- [ ] Private encrypted storage, secure uploads, quarantine/scanning, isolated parsers, limits and ephemeral-password behavior are verified.
- [ ] Consent notices, optional AI/CA scopes and withdrawal behavior are implemented and reviewed.
- [ ] Approved retention durations, export/deletion workflows, derivative/processor handling and backup residual-retention disclosures are implemented and tested.
- [ ] Independent security review is complete with no unresolved critical/high findings.
- [ ] Qualified privacy/legal review covers applicable obligations and processors; no unverified compliance claim is published.
- [ ] Backups restore correctly, deletion records are reapplied, and monitoring/support/incident escalation have responsible contacts.
- [ ] No customer data is copied into Git, issues, PRs, logs or general-purpose support channels.

Until these pass, internal demonstrations and interviews use safe synthetic material. Day 60 is not authorization to collect real statements.

## Before Day 75 release-candidate approval target

For tax/CA gates below, use the proposed [period/document scenarios](tax/DOCUMENT_READINESS.md) and [sharing failure cases](research/DAY_03_CA_WORKFLOW.md) as inputs to independent review and implementation testing. These examples have not run and no gate is checked by DAY-003 documentation or a later milestone scope amendment. External review tasks are recorded in the [CA discovery pack](research/DAY_03_CA_DISCOVERY.md).

- [ ] Every advertised bank/card format/version is selected from suitable fixtures and passes extraction/reconciliation tests; unsupported/scanned files fail gracefully.
- [ ] Independent golden fixtures pass exactly for income, consumption, investments, transfers, card purchases/repayments, refunds/reversals, cash flow and qualified savings.
- [ ] Re-import/overlap protection preserves legitimate repeated purchases; corrections/undo and provenance are verified.
- [ ] Partial coverage, missing balances, period filters and source drill-downs remain correct in dashboards, reports, exports and AI results.
- [ ] Recurring/anomaly evaluation reports describe corpus, precision/recall or case outcomes and limitations.
- [ ] AI numerical/source checks and privacy/injection cases pass; costs/quotas are server-enforced and provider terms reviewed.
- [ ] Tax checklist and every published policy item have appropriate source/applicability/version and qualified approval; rollback passes.
- [ ] CA sharing tests cover selected resources, recipient binding, expiry, revocation, forwarded links and audit; downloaded-copy limitations are disclosed.
- [ ] Payment sandbox tests cover signatures, replays, duplicates, out-of-order delivery, failures, receipts, refunds, cancellation and entitlement expiry.
- [ ] CI includes application tests, lint/type checks, financial/security regression and dependency/secret scans; tracker-only CI is insufficient.
- [ ] Approved performance workload/budgets pass; accessibility and mobile core journeys pass review.
- [ ] Backup/recovery and deployment rollback are rehearsed within approved objectives.
- [ ] Independent review findings are remediated and retested; privacy and operational evidence above remains current.

The Day 75 target depends on reviewer availability and remediation. If a gate fails, move the milestone rather than use real customers to discover a known unsafe condition.

## Controlled beta: Days 76–80 target

- [ ] Real-data gate and release-candidate evidence approved; bounded consenting cohort and support capacity agreed.
- [ ] Verify import quality, report comprehension, correction burden and CA package usefulness with consent and minimal telemetry.
- [ ] Validate controlled production payment/refund behavior before broader paid access; never use sandbox results as production evidence.
- [ ] Record incidents, refusals, unsupported formats and defects; pause affected functionality or collection when a safety gate regresses.
- [ ] Obtain actual user feedback; do not present scripted demonstrations as customer research.

## Public launch: Day 85 target

- [ ] All applicable gates remain passed for the release build; no unresolved critical/high security or financial-correctness blocker.
- [ ] Controlled-beta evidence supports advertised capabilities; known limitations and supported formats are public.
- [ ] Pricing, entitlements, renewal/refund terms, receipts and legal disclosures approved.
- [ ] Working brand clearance/domain/legal-entity questions resolved for public marketing; configurable branding preserved.
- [ ] DAY-004 [regulatory follow-ups](REGULATORY_REVIEW.md) have dated applicability decisions, including the 2026 consumer amendment, privacy phases/retention and CA engagement boundaries; relevant safeguards are tested, not inferred from research.
- [ ] [Brand findings](BRANDING.md) are professionally resolved before public brand expenditure; name use in configuration is not clearance.
- [ ] Production alerts, recovery, support and rollback contacts verified in a final rehearsal.
- [ ] Owner records explicit go/no-go and independent financial/tax/security/privacy reviews as applicable.

## DAY-001 is a separate acceptance gate

DAY-006's [local scaffold evidence](DAY_06_FOUNDATION.md) is also a separate review artifact. A passing synthetic UI/build/health check is not release approval. Waitlist, actual ledger/migrations/authentication, independent privacy/security/tax reviews and production operations remain subject to the gates above. Confirm the DAY-006 issue through a successful lookup, review the diff and remote CI, and obtain explicit human acceptance before verification. No completion checkbox is changed here.

This documentation draft does not satisfy product release gates or mark Day 1 complete. DAY-001 requires human review of its [deliverables](DAY_01_KICKOFF.md), reviewed/merged PR and passing CI per [AGENTS.md](../AGENTS.md), plus explicit owner authorization before Issue #1 is labeled verified and closed. No automated closure or verification is authorized.

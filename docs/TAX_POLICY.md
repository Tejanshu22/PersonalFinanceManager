# FINNest — tax-content and readiness governance

**DAY-001 review draft · 2026-10-10. No tax content has been professionally approved for product publication.**

V1 organizes user-uploaded documents, identifies gaps against a reviewed checklist and presents limited source-linked policy information. It does not calculate final liability, recommend a tax regime, guarantee completeness, file ITR/GST returns or interpret law autonomously. A bank receipt category is not a tax-income determination.

## Official reference and period boundary

The [Income Tax Department transition FAQ](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/objective-and-scope-new-act-faq), consulted on 2026-10-10, describes the Tax Year convention applying from 1 April 2026 and continued treatment of earlier periods under the previous framework. For example, FY 2025–26 / AY 2026–27 must not be relabeled merely because a document was uploaded after April 2026; Tax Year 2026–27 uses the newer convention.

This reference supports period-model planning, not a full legal interpretation or reviewed tax rule set. A qualified tax reviewer must verify each published applicability example against operative legislation, notifications and transitional provisions. Preserve historical labels and source framework; never infer governing law solely from upload date.

## Minimal versioned policy record

For every published checklist rule or policy item, retain:

- Stable internal ID, statutory framework, relevant sections and authoritative source URL/document reference.
- Publication date, effective applicability start/end, tax-period type/identifier and supported income circumstances; distinguish these dates.
- Structured content, explanatory limitations, version and source snapshot/hash where permitted.
- Author, qualified reviewer identity/qualification, decision, approval timestamp and review notes.
- Superseded-by references, publication status, change reason and rollback target.
- Cases and expected readiness output used for approval, with no customer identifiers.

Store historical versions; do not overwrite rules previously used in a report. Readiness/report snapshots identify the approved version and user declarations used. Correcting source metadata creates history rather than destroying provenance.

## Publication and rollback

Official source → draft structured content → qualified tax review → approve/reject → versioned publication → monitored review for changes.

Unapproved, expired or uncertain applicability must not silently affect user output. Fail with an explicit unsupported/pending-review state where no suitable approved version exists. Publication and rollback require authorized reviewer approval and audit; rollback selects a known approved version and flags affected reports for review. It does not silently rewrite already exported packages.

V1 may use a small protected editorial workflow; governance remains mandatory even if no sophisticated admin platform is built. Review frequency and update-response time must be agreed with the appointed reviewer before publication.

## Tax readiness behavior

- Use declared income sources, period and available documents to explain each required, missing, received, user-confirmed or unresolved item.
- Form 16 metadata is source-linked and user-reviewable. AIS/TIS identification/tagging does not imply complete tax reconciliation.
- A received file is not proof of correctness, authenticity or sufficient tax disclosure. Unknown/unsupported income circumstances must remain unresolved.
- Prefer status plus reasons over a percentage suggesting tax certainty. Even a complete supported checklist means “documents present for this checklist,” not “ready to file” or “no tax due.”
- CA exports include period, documents selected, declaration limitations, reconciliation/coverage gaps and questions requiring professional attention.
- Do not expose PAN/full document content to hosted AI. AI cannot approve policy or make personalized tax determinations.

## Review dependencies and evidence

The product owner must appoint a qualified tax reviewer, agree supported periods/scenarios and budget review time before tax content is enabled. Require independently reviewed synthetic scenarios for old/new periods, missing/mismatched documents, multiple income types, superseded rules and rollback. All approved scenarios must produce expected results, and every published item must have complete approval/source metadata.

External legal advice is separately required for the product's service boundaries, disclaimers, data handling and any future authorized integration. No tax-portal credentials/OTP scraping, unofficial login automation or assumed ERI eligibility. Advanced tax computation, gains parsing, regime comparisons and direct filing remain later releases and require new approval.

See [open decisions](DECISIONS.md), [security requirements](SECURITY.md) and [acceptance journey 10](REQUIREMENTS.md).
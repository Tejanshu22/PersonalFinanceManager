# FINNest — business model and validation plan

**DAY-001 review draft · 2026-10-10. Pricing and demand are unvalidated hypotheses.** No interviews, market sizing, conversion results or profitability findings are asserted.

## Customer and value journey

The initial buyer is an Indian salaried individual who needs understandable multi-account finances and organized tax documents. Salary plus supplementary freelance income is the secondary segment. A CA receives a scoped package in V1; a CA practice subscription is a later business model.

**Upload → Reconcile → Correct → Understand → Prepare Tax Documents → Share with CA → Upgrade.** The free experience should demonstrate useful, trustworthy output before an upgrade. Explain unsupported formats before payment. Payment does not improve the truthfulness of calculations or remove mandatory warnings.

## Pricing and packaging hypotheses

| Offer | Price hypothesis | Candidate value and unresolved boundary |
| --- | ---: | --- |
| Free | ₹0 | Limited supported imports, basic dashboard, corrections and monthly summary. Exact account/import/history limits pending cost and interview evidence. |
| Plus | ₹999/year | Greater multi-account capacity/history, recurring candidates, Ask My Money allowance, tentative unusual-charge insights and richer reports. No deferred price-increase alerts, health components or reminders promised. |
| One-time Tax Pack | ₹499 | Readiness checklist and CA-ready package/sharing; not tax computation or filing. Proposed purchase unit: one named reporting period with repeat corrections/exports during a disclosed access window; approval pending. |
| Advanced Tax / Tax Pro | ₹1,999/year | Later professionally validated tax capabilities; not a V1 checkout offer. |
| CA Workspace | Not set | V2 practice workflow subscription only after professional discovery and pilot value evidence. |

The base tax-document vault, basic readiness visibility, package export and sharing entitlement split needs approval; do not implement conflicting paywalls from this draft. Resolve whether Plus includes a Tax Pack or offers it separately, access-window duration, usage limits and post-expiry behavior. Do not repeatedly charge users to correct an erroneous package.

Proposed trust floor: existing-data viewing/correction, mandatory warnings, privacy controls, consent withdrawal, revocation, deletion and own-data export remain accessible without upgrading. Paid limits control additional processing/capacity, not ownership of uploaded data. Owner approval is pending for the final entitlement matrix.

## Conversion, retention and costs

Hypothesized conversion moments: a user successfully reconciles a first statement then needs more accounts/history; identifies useful recurring commitments; or needs an organized CA package. Test willingness to pay only after explaining import effort, coverage limitations and data handling. Annual Plus can provide recurring revenue only if renewal value exists; a Tax Pack is seasonal transactional revenue. Auto-renewal versus explicit renewal is undecided and must be disclosed before purchase.

Monthly statement re-import and report comprehension are potential retention drivers. Seasonal tax use may not support annual renewal. Do not introduce reminders back into V1 to claim retention. Do not sell financial data or use undisclosed financial-product targeting, investment recommendations, brokerage commissions or implicit CA fee splitting.

Track hosting/database, encrypted object storage/backups, scanning and parsing, queue traffic, model tokens, email, payment fees, refunds/chargebacks, support time, legal/tax/security review and acquisition. Set free and paid processing limits only after representative cost measurements. A ₹999 selling price is not margin; model applicable taxes and all costs, including founder support time.

Contribution per paid customer should use net receipts after applicable taxes/refunds minus attributable processing, payment and support costs; fixed professional/hosting costs remain visible separately. Profitability needs both variable and fixed costs covered. No unsupported market size, conversion percentage or break-even claim is permitted.

## Measurement definitions (targets pending evidence)

| Measure | Definition | Interpretation |
| --- | --- | --- |
| Reconciled activation | Verified registrants achieving a finalized reconciled import and completed transaction review within 7 days / verified registrants with a full 7-day observation window | Report reconciliation-unavailable imports separately; do not count them as reconciled |
| Import success | Supported-format attempts finalized without extraction errors / supported-format attempts | Report reconciliation, retries, unsupported formats and user cancellations separately |
| Next-month retention | Activated users making another finalized import in the next calendar month / activated users with a complete next-month observation window | Segment by first format and persona; small samples are not market evidence |
| Free-to-paid | First-time paying users / free users exposed to an eligible offer in a stated cohort/window | Distinguish Plus and Tax Pack; exclude test payments |
| Annual renewal | Renewed subscriptions / subscriptions actually eligible for renewal in the stated window | Cannot be validated during an 85-day build |
| Package usefulness | Interviewed package users/CAs who can complete predefined review tasks, with observed issues and reported time | Self-reported time savings are not independently measured savings |
| Unit economics | Net receipts, variable cost, support time, fixed cost and refunds per cohort | No sensitive transaction contents in telemetry |

Use opaque event IDs and coarse outcomes; no raw financial content or account identifiers in analytics. Early cohorts establish baselines, not invented success rates.

## Validation questions and experiments

Days 2–3: interview ten genuine prospects across the two individual personas and two CAs, following [the interview guide](DAY_01_KICKOFF.md). Ask about the last real statement/tax-document workflow before showing the concept.

- Would the person upload at all? What trust evidence, deletion controls, provider choice or AI opt-out changes that decision?
- Can they explain a synthetic report's income, spending, transfers, repayments and coverage warning correctly?
- Does correcting an import feel less burdensome than their current workaround?
- Which formats can they export, without providing financial documents during discovery?
- After the value demonstration, would they choose free, ₹999/year Plus, ₹499 Tax Pack, neither or another arrangement? What existing alternative would it replace?
- Does one reporting-period Tax Pack feel clearer than “per use”? Should Plus include it?
- Would a CA use the package, and what missing evidence would make it unusable?
- Would they return next month? What concrete event prompts return without automated reminders?

Record objections and refusals, not only favorable comments. A hypothetical yes is weaker evidence than later voluntary paid use; no sales or payment collection during interviews. Revisit packaging after interviews and controlled-beta cost evidence. Receipts, tax treatment, consumer disclosures, refunds and merchant approval require owner and qualified professional review before paid release.
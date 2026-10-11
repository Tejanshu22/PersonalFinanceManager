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

## Preliminary survey evidence — 2026-10-11

The [pilot report](research/DAY_02_SURVEY_PILOT.md) contains five hypothetical annual-price answers: the three employed respondents chose different bands (one up to ₹499, one ₹500–₹999, one ₹1,000–₹1,999); both students were uncertain until a trial. These are reported choices, not purchases, conversion or a validated ₹999 price. The annual bands do not test the separate ₹499 one-time Tax Pack, entitlement split or renewal behavior. One respondent gave conflicting paid-service selections; their subgroup is unspecified, so no clean nonpayment total is inferred.

All prices and packaging above remain unchanged hypotheses. Interview follow-ups must establish actual past purchases, the job delivered, current alternatives, upload effort and seasonal versus recurring value. See the [evidence register](DAY_02_RESEARCH_SUMMARY.md); no paid pilot, outreach or real-document collection is authorized by this survey integration.

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

External follow-up: FIN-002 still requires ten real prospect interviews; the founder-approved Day 2 survey amendment does not supply them. Two CA interviews and professional review also remain pending under [Day 3 discovery](research/DAY_03_CA_DISCOVERY.md). Use [the interview guide](DAY_02_INTERVIEW_GUIDE.md), asking about the last real statement/tax-document workflow before showing the concept. These conversations can proceed alongside design; they are not falsely recorded as completed Days 2–3 work.

- Would the person upload at all? What trust evidence, deletion controls, provider choice or AI opt-out changes that decision?
- Can they explain a synthetic report's income, spending, transfers, repayments and coverage warning correctly?
- Does correcting an import feel less burdensome than their current workaround?
- Which formats can they export, without providing financial documents during discovery?
- After discussing current problems and explaining the proposed value and limitations, would they choose free, ₹999/year Plus, ₹499 Tax Pack, neither or another arrangement? What existing alternative would it replace?
- Does one reporting-period Tax Pack feel clearer than “per use”? Should Plus include it?
- Would a CA use the package, and what missing evidence would make it unusable?
- Would they return next month? What concrete event prompts return without automated reminders?

Record objections and refusals, not only favorable comments. A hypothetical yes is weaker evidence than later voluntary paid use; no sales or payment collection during interviews. Revisit packaging after interviews and controlled-beta cost evidence. Receipts, tax treatment, consumer disclosures, refunds and merchant approval require owner and qualified professional review before paid release.

## DAY-004 pricing assessment — proposals, not approved changes

Research dated **2026-10-11** is in the [market analysis](research/DAY_04_MARKET_ANALYSIS.md). Free connected tracking and low-cost tax-filing offers challenge both Plus and Tax Pack. A readiness-only package cannot claim equivalent value to filing simply because it costs less. FIN-004's tested-pricing acceptance remains unmet: no purchases, paid pilot, observed renewal or controlled pricing experiment is documented.

Keep all five existing price hypotheses unchanged. Propose Free deliver one meaningful supported/reconciled month with corrections, source drilldown, coverage warnings and an understandable summary; capacity limits need measured cost evidence. Plus should charge for sustained multi-account/history use and bounded additional analysis, not correctness, deletion or access to existing records. Tax Pack could sell a reusable package for a named reporting period with controlled sharing and repeated corrections during a disclosed window. Its differentiation must be demonstrated to the user's existing CA; no filing, advice or appointed CA is included by default. Decide whether Plus includes a pack before displaying either offer publicly.

Annual-only billing lowers transaction frequency but asks an unfamiliar user to trust a year of value before experiencing it. Test annual versus a clearly described one-time report concept; a monthly option is another research question, not an added SKU. A standalone report risks cannibalizing Free/Plus and must not charge to fix product errors. No price for either new option is approved. Seasonal use might support Tax Pack without annual Plus retention; don't build reminders or full CA SaaS to conceal that uncertainty.

### Hypothetical first-year cohort model

These are **illustrative stress scenarios, not forecasts, market benchmarks or spending authority**. All acquisition, activation, conversion, retention and cost figures are invented model inputs, explicitly unvalidated. “Optimistic” means favorable demand assumptions, not guaranteed profit. Each cohort is followed for twelve months from signup; no ramp, financing or accounting revenue-recognition schedule is modeled. Annual service cost is charged in full. The model is not the 85-day delivery budget.

Plus and Tax Pack buyers are disjoint subsets of activated users: nobody is charged/counts in both. Nonbuyers include inactive registrants. All paid amounts are assumed successfully settled; failed attempts produce no revenue. A 3% proportional refund assumption covers refunds only, not a validated chargeback rate. Year-two renewal assumptions are shown but produce no year-one revenue. The hypothetical second-month retention does not reduce the annual cost inputs again.

| Assumed input | Conservative | Base Case | Optimistic |
| --- | ---: | ---: | ---: |
| Unique acquired landing visitors | 5,000 | 20,000 | 80,000 |
| Signup rate / registrants | 10% / 500 | 10% / 2,000 | 10% / 8,000 |
| Activation / activated users | 20% / 100 | 30% / 600 | 40% / 3,200 |
| Plus buyers / activated conversion | 5 / 5% | 60 / 10% | 800 / 25% |
| Additional Tax Pack buyers / activated conversion | 5 / 5% | 40 / 6.67% rounded | 200 / 6.25% |
| Next-month retained / activated | 20% | 35% | 50% |
| Eventual eligible Plus renewal, year two only | 30% | 50% | 70% |
| Plus annual / Tax Pack one-time price | ₹999 / ₹499 | ₹999 / ₹499 | ₹999 / ₹499 |
| Annual cost per nonbuyer | ₹12 | ₹18 | ₹24 |
| Annual processing per Plus / per pack buyer | ₹60 / ₹30 | ₹90 / ₹45 | ₹120 / ₹60 |
| Support per buyer, minutes at ₹300/hour | 30 | 20 | 15 |
| Fixed annual hosting/base operations | ₹60,000 | ₹90,000 | ₹120,000 |
| Annual legal/security/tax-review allowance | ₹60,000 | ₹90,000 | ₹120,000 |
| Cash acquisition budget | ₹10,000 | ₹30,000 | ₹60,000 |
| Founder non-support labor allowance | ₹300,000 | ₹300,000 | ₹300,000 |

Cost allowances are not supplier quotes and may be insufficient. Per-user processing includes scanning/parsing retries, AI use, encrypted storage/backups and messages; nonbuyer cost also includes averaged free support. Paid support is separate. Fixed hosting covers baseline services only, avoiding double-counting marginal usage. Founder non-support allowance includes acquisition/design/operations time; buyer support is excluded from it. More use can increase costs, hence the higher per-user processing stress assumptions at scale.

For this sensitivity only, prices are assumed **inclusive of 18% output tax**, with refunds reducing the taxable amount; no input-tax credit is assumed. FINNest's actual GST registration, rate, invoice and refund treatment require CA advice and could differ. Payment-fee assumption is **2% plus 18% tax on that fee = 2.36% of gross settled receipts**, with no recovery of original processing fees on refund. This is a model input, not a gateway quote. [Razorpay's current page](https://razorpay.com/pricing/), accessed 2026-10-11, contains promotional and method-specific pricing (including a displayed 2.15% + GST platform fee); obtain a written quote and rerun the model before selecting a provider. Recurring mandates, international methods, chargebacks and special services can change costs.

| Calculated first-year result, INR | Conservative | Base Case | Optimistic |
| --- | ---: | ---: | ---: |
| Gross settled receipts | ₹7,490.00 | ₹79,900.00 | ₹899,000.00 |
| Refund allowance, 3% | ₹224.70 | ₹2,397.00 | ₹26,970.00 |
| Net revenue after refunds/assumed output tax | ₹6,157.03 | ₹65,680.51 | ₹739,008.47 |
| Payment fees including assumed fee tax | ₹176.76 | ₹1,885.64 | ₹21,216.40 |
| Nonbuyer subsidy | ₹5,880.00 | ₹34,200.00 | ₹168,000.00 |
| Buyer processing | ₹450.00 | ₹7,200.00 | ₹108,000.00 |
| Buyer support labor | ₹1,500.00 | ₹10,000.00 | ₹75,000.00 |
| Cohort contribution after all variable costs | −₹1,849.73 | ₹12,394.87 | ₹366,792.07 |
| After fixed costs and cash acquisition, before founder non-support labor | −₹131,849.73 | −₹197,605.13 | ₹66,792.07 |
| Economic result including founder non-support labor | **−₹431,849.73** | **−₹497,605.13** | **−₹233,207.93** |

Reproducible formulas: `gross = 999 × Plus + 499 × packs`; `net = gross × 0.97 / 1.18`; `fee = gross × 0.0236`; `free = (registrants − Plus − packs) × nonbuyer cost`; `processing = Plus × Plus cost + packs × pack cost`; `support = (Plus + packs) × minutes / 60 × 300`. Contribution is net less fee/free/processing/support. Deduct both fixed allowances, acquisition and founder labor for the economic result. Calculations use Python Decimal with exact decimal inputs, rounding displayed INR to two decimals only at the end. Conversion counts are primary; the 6.67% display is rounded, not used to derive buyers.

Interpretation: none of these cohorts funds all modeled work. The optimistic case covers its assumed cash/fixed costs but not the founder labor allowance. This does not prove the business cannot work; it shows that ₹999 revenue alone is not profitability and that free-user subsidy, human support and acquisition matter. An extra ten minutes of paid support at the modeled labor rate costs ₹50 per buyer. A one-percentage-point processing-fee increase costs 1% of gross receipts. Measure real costs and revise hypotheses before calculating a credible break-even point or customer lifetime value. Reserves for unmodeled disputes or unexpectedly expensive reviews would worsen the results.

### Experiments requiring founder approval and real behavior

| Experiment | What to observe | What does not validate it |
| --- | --- | --- |
| Sample report comprehension and upload decision | Can target users distinguish income/spending/transfers, spot missing coverage, and explain informed upload refusal/acceptance? Start with synthetic data | Positive landing-page reaction or selected privacy features |
| Annual Plus versus seasonal Tax Pack concept | Recent job, alternative replaced, preferred entitlement/access window and reason for choosing neither | Hypothetical price-band selection; two students do not represent employed buyers |
| Later bounded paid beta, approved price/terms only | Voluntary settled non-test purchases after useful output; eligible-offer denominator, support/refunds, repeat use | Checkout clicks, free trials or founder-subsidized purchases |
| One-time report versus annual commitment | Whether occasional users pay for a defined output without reducing total contribution; price/limits require approval first | Invented demand, an unimplemented “buy” button implying availability |
| Renewal/retention follow-up | Next-month work and eventual renewal among eligible subscribers, segmented by persona/offer | Annual renewal forecast treated as observed retention |

Predeclare sample/window, loss cap, stopping rules and success criteria with the founder before collecting payments. No experiment is conducted here. Interview refusals and failed tasks are evidence; changes to approved prices, entitlements or releases require a separate decision.

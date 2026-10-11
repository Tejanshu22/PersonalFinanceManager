# DAY-004 — market, positioning and commercial discovery

**Issue #12 · research date/access date: 2026-10-11 · founder review draft.** FINNest is planned, not built. Public product documentation confirms advertised offerings, not tested quality, uptime, security or customer demand. Prices are public observations, not checkout quotes. No paid account, competitor upload or customer financial document was used.

## Repository and evidence boundary

Reviewed AGENTS.md, README, requirements, monetization, security, tax policy, architecture, decisions, release checklist, screens, branding configuration, Day 2/3 research and both source manifests. The worktree began clean on `master`. DAY-004 calls for competitor, pricing, compliance and name analysis. FIN-004 also requires **tested price hypotheses**: desk research and arithmetic cannot satisfy that behavioral evidence requirement. Issue #12 could not be read through GitHub CLI because the request timed out; its current remote acceptance/labels remain unconfirmed.

The approved scope remains 140 V1 / 14 V1.5 / 20 V2 / 8 V3+ / 12 Future, total 194; 85 working days, Day 60 internal beta and conditional Day 85 public launch. No roadmap/source/generated change is proposed here. Earlier [decisions](../DECISIONS.md) retain unresolved roadmap dependency proposals and Day 3 acceptance amendment D3-01. Local generated status now shows Days 1/2 Verified Done and Days 3/4 Planned; that is a cached tracker display, not independently inspected approval evidence. Earlier publication-pending notes describe historical snapshots.

The [Day 2 pilot](DAY_02_SURVEY_PILOT.md) is five genuine responses: three employed people (two salaried, one salary plus freelance) and two students. Employed respondents raised transaction confusion, tax-reporting uncertainty and upload effort; concerns about access visibility span the pilot. Preserve dissent, straightforward filing/no-recent-problem answers and the contradictory paid-service answer. This is exploratory evidence, not prevalence or willingness-to-pay proof. Actual customer interviews, two CA interviews and professional approval remain pending. [Day 3 workflow](DAY_03_CA_WORKFLOW.md) and [readiness rules](../tax/DOCUMENT_READINESS.md) remain hypotheses requiring review.

## Competitor findings

**Evidence types:** fact = explicitly documented public offering; claim = vendor assertion about outcomes/quality; inference = our strategic interpretation; unknown = not verified. Every source below was accessed on **2026-10-11**. An active website is evidence of a public offering, not proof of onboarding availability for every user.

| Product and target/problem | Documented approach and capabilities | Revenue/price observation | Advantage, limitation and overlap |
| --- | --- | --- | --- |
| INDmoney — individuals consolidating banking and investments | Bank-linked transaction/category/cash-flow views; AA/depository connections. Read-only Claude integration answers portfolio questions; tax computations are expressly outside that connector. General bank-file import and selective own-CA sharing unknown. [I1–I3 below] | Bank/net-worth tracking advertised free; broader investing platform. Exact brokerage/product revenues not audited | Inference: strong free dashboard substitute. Connector has narrower portfolio scope than arbitrary financial questions. “Free” and accuracy/security claims do not establish independent verification |
| Fold Money, India — people tracking accounts and spending | AA bank connections, categorization and cash flow. Recurring suggestions need user setup/review and can produce false positives. Current MCP beta exposes read-only finance tools to authorized AI apps; annual Plus/Believer restricted. [F1–F5] | Free and Plus documented. Launch blog quotes regular ₹2,999/year and staged discounts; **historical offer, current checkout price not verified** [F6–F7] | Closest workflow competitor; convenience reduces manual upload. Bank/card coverage and refresh dependencies remain. AI and recurring detection are already competitive capabilities; older Radar rollout promises are not evidence of universal availability |
| ET Money — investment tracking, execution and advisory customers | Current product update emphasizes external mutual-fund tracking/portfolio health and distinction between Genius advisory and direct-plan execution. Current bank-statement expense tracking, AI questions and own-CA workflow unknown. [E1–E2] | Paid Genius membership; current price not verified | Inference: indirect wealth/attention competitor. Vendor describes complexity and regulatory separation affecting tracking/health access; do not attribute historical expense features to today's app |
| axio — expense-management and consumer-credit users | Current site advertises spending categorization/limits; FAQ describes Android transactional-SMS ingestion and manual entry when a message is missed. Statements exported by email are not evidence of PDF import. [A1–A2] | Lending/BNPL including Amazon Pay Later advertised; standalone PFM subscription price not verified | Inference: low-input expense substitute, different credit-led business. SMS availability/pattern coverage constrain capture. Cash-wallet exclusion helps avoid double-counting but does not prove automatic own-account transfer matching |
| ClearTax — taxpayers needing DIY or assisted filing | Tax-document intake, preparation/filing and assigned experts; own-CA granular sharing and year-round statement analytics unknown. [C1] | Assisted salary/house-rent FAQ starts ₹1,299; gains/self-employment from ₹3,999. Offer scope, taxes and checkout need confirmation | Filing and professional assistance deliver a more terminal outcome than readiness. Inference: major seasonal alternative; low price alone cannot justify FINNest Tax Pack |
| TaxBuddy — DIY and assisted taxpayers | Public site markets AI self-filing, document upload and expert support. “100% accuracy” is a vendor claim, not independently verified. AI tax preparation does not establish open-ended bank-data Q&A. [T1–T2] | Listed salary plus one-house plan ₹999/year, taxes extra; eligibility/checkout must be confirmed | Inference: strong tax-season substitute. Assigned professional help is not evidence of access scoped to a user's existing CA |
| Quicko — taxpayers organizing and filing online | Save/pay/file tax workflow with connections and income-plan eligibility. Statement-level personal-finance analytics and own-CA permissions not verified. [Q1–Q2] | Basic free up to ₹12 lakh, one connection; Essential ₹999 single pass up to ₹24 lakh/three connections; Elite ₹1,499 single pass. Tax inclusion not established | Free entry and task-specific purchase pressure seasonal pricing. Plan ceilings are documented limits; a single pass is not an annual subscription |
| Income Tax Department e-Filing portal — self-filing taxpayer | Official return preparation/filing, tax statements and reporting-period guidance. Separate legal filing workflow, not a verified multi-bank analytics/CA-package substitute. [G1–G2] | Government DIY route; no commercial software plan compared here | Inference: an indirect alternative to paying for organization; complexity or user dissatisfaction cannot be assumed without observed tasks |
| Spreadsheet/folders plus existing CA — current workaround | A workflow hypothesis to test in interviews, not a standardized vendor product; capabilities depend on the person/template | Software and professional cost vary; not measured | Familiarity/control can outweigh an app's automation. Ask for recent time and error examples before claiming superiority |

### Source register

Each link records the exact observed URL; all access dates are 2026-10-11. Help pages/blogs may describe a dated rollout; limitations above preserve that distinction.

| Ref | Official source and observation |
| --- | --- |
| I1 | [INDmoney bank tracking](https://www.indmoney.com/networth/track-bank-accounts) — bank transactions and cash-flow offering |
| I2 | [INDmoney net worth](https://www.indmoney.com/networth) — connections/free dashboard claim |
| I3 | [INDmoney MCP](https://www.indmoney.com/mcp) — read-only portfolio AI, connection consent/revocation and scope limitations |
| F1 | [Fold India](https://fold.money/) — connected personal finance; distinct from US `foldapp.com` |
| F2 | [Fold recurring suggestions](https://help.fold.money/hc/en-us/articles/22026039651602-What-are-recurring-suggestions-and-how-do-I-use-them) — reviewed candidates/false positives |
| F3 | [Fold MCP](https://help.fold.money/hc/en-us/articles/39033616914194-What-is-Fold-MCP-and-how-do-I-set-it-up) — updated 2026-09-17, restricted experimental beta |
| F4 | [Supported credit cards](https://help.fold.money/hc/en-us/articles/17395390205586-Supported-Credit-Cards) — coverage/plan dependency |
| F5 | [Investment known issues](https://help.fold.money/hc/en-us/articles/17447540222866-Known-Issues-Investments) — dated limitations, not fresh runtime tests |
| F6 | [Is Fold free?](https://help.fold.money/hc/en-us/articles/17262017781522-Is-Fold-a-free-app) — free/paid distinction |
| F7 | [Price of free software](https://fold.money/blog/price-of-free-software) — historical launch pricing, not verified current quote |
| E1 | [Reimagining ET Money](https://www.etmoney.com/learn/product-updates/reimagining-et-money/) — investment positioning and access changes |
| E2 | [Genius membership](https://www.etmoney.com/help/genius/membership) — subscription offering |
| A1 | [axio](https://www.axio.co.in/) — public PFM and lending offerings |
| A2 | [axio FAQ](https://www.axio.co.in/faq?5b88f6dd_page=2) — SMS/manual capture limitations |
| C1 | [ClearTax pricing](https://cleartax.in/s/pricing) — assisted-filing scope and starting prices |
| T1 | [TaxBuddy](https://www.taxbuddy.com/) — AI/assisted tax claims |
| T2 | [TaxBuddy ITR pricing](https://www.taxbuddy.com/itr-price) — listed plans; generic `/pricing` fetch failed |
| Q1 | [Quicko](https://quicko.com/) — current tax workflow |
| Q2 | [Quicko pricing](https://quicko.com/pricing) — eligibility, free and single-pass plans |
| G1 | [Official e-Filing portal](https://www.incometax.gov.in/iec/foportal/) — government alternative |
| G2 | [ITR-1 guidance](https://www.incometax.gov.in/iec/foportal/help/e-filing-itr1-form-sahaj-faq) — return/period-specific help; not universal applicability |

## Capability comparison

Labels are literal: **Confirmed Available** = explicitly documented offering, not independently exercised; **Confirmed Unavailable** = explicit exclusion, never silence; **Partial / Restricted** = limited scope/eligibility; **Not Verified** = insufficient evidence; **FINNest Planned — Not Built** = specification only. No matrix absence has enough evidence to assert Confirmed Unavailable. File import means user-supplied bank/card transactions, not exporting statements or uploading Form 16. Privacy row concerns documented user controls, not a security rating. Generic tax filing is not a readiness checklist.

| Capability | FINNest V1 | INDmoney I1–I3 | Fold F1–F7 | ET Money E1–E2 | axio A1–A2 |
| --- | --- | --- | --- | --- | --- |
| CSV statement import | FINNest Planned — Not Built | Not Verified | Not Verified | Not Verified | Not Verified |
| PDF statement import | FINNest Planned — Not Built; one bank/one card | Not Verified | Not Verified | Not Verified | Not Verified |
| Transaction categorization | FINNest Planned — Not Built | Confirmed Available | Confirmed Available | Not Verified | Confirmed Available |
| Internal transfer detection | FINNest Planned — Not Built | Not Verified | Not Verified | Not Verified | Not Verified |
| Combined spending/income analytics | FINNest Planned — Not Built | Confirmed Available | Confirmed Available | Not Verified | Partial / Restricted; spending verified |
| Recurring-payment detection | FINNest Planned — Not Built | Not Verified | Partial / Restricted; reviewed suggestions | Not Verified | Not Verified |
| AI financial questions | FINNest Planned — Not Built | Partial / Restricted; portfolio connector | Partial / Restricted; paid MCP beta | Not Verified | Not Verified |
| Tax-document organization | FINNest Planned — Not Built | Not Verified | Not Verified | Not Verified | Not Verified |
| Period-specific tax-readiness information | FINNest Planned — Not Built | Not Verified | Not Verified | Not Verified | Not Verified |
| CA-ready document packages | FINNest Planned — Not Built | Not Verified | Not Verified | Not Verified | Not Verified |
| Selective own-CA access | FINNest Planned — Not Built | Not Verified | Not Verified | Not Verified | Not Verified |
| Privacy/data controls | FINNest Planned — Not Built | Partial / Restricted; AI grant revocation documented | Partial / Restricted; AI grant revocation documented | Not Verified | Not Verified |
| Pricing | FINNest Planned — Not Built | Confirmed Available; free tracking | Partial / Restricted; free/paid, current quote unknown | Partial / Restricted; paid, quote unknown | Not Verified; PFM price |

| Capability | ClearTax C1 | TaxBuddy T1–T2 | Quicko Q1–Q2 | Official portal G1–G2 |
| --- | --- | --- | --- | --- |
| CSV statement import | Not Verified | Not Verified | Not Verified | Not Verified |
| PDF statement import | Not Verified | Not Verified | Not Verified | Not Verified |
| Transaction categorization | Not Verified | Not Verified | Not Verified | Not Verified |
| Internal transfer detection | Not Verified | Not Verified | Not Verified | Not Verified |
| Combined spending/income analytics | Not Verified | Not Verified | Not Verified | Not Verified |
| Recurring-payment detection | Not Verified | Not Verified | Not Verified | Not Verified |
| AI financial questions | Not Verified | Partial / Restricted; AI tax-filing claim | Not Verified | Not Verified |
| Tax-document organization | Partial / Restricted; filing intake | Partial / Restricted; filing intake | Partial / Restricted; tax records/connections | Partial / Restricted; official statements/returns |
| Period-specific tax-readiness information | Not Verified | Not Verified | Not Verified | Partial / Restricted; guidance, not FINNest checklist |
| CA-ready document packages | Not Verified | Not Verified | Not Verified | Not Verified |
| Selective own-CA access | Not Verified | Not Verified | Not Verified | Not Verified |
| Privacy/data controls | Not Verified | Not Verified | Not Verified | Not Verified |
| Pricing | Confirmed Available; starting offers above | Confirmed Available; eligibility/tax limits above | Confirmed Available; free/single pass above | Partial / Restricted; official DIY, no comparable plan |

Unknown cells need hands-on, permission-safe product review or written vendor clarification before a public comparison. Do not publish “only FINNest does this.” Tax-filing competitors' intake/assigned experts overlap the handoff problem but do not demonstrate the exact proposed selective-sharing control.

## Positioning recommendation — interpretation, not validated demand

| Consideration | A: AI personal finance tracker | B: Financial clarity and money intelligence | C: Finance + tax readiness + CA handoff |
| --- | --- | --- | --- |
| Value clarity | Technology-led; users must infer outcome | Clear if anchored to a specific confusing month | Strong end task but long, complicated initial promise |
| Urgency | Curiosity may dominate | Recent unexpected cash-flow/savings change | Strong near tax preparation; seasonal |
| Payment hypothesis | Weak without unique grounded answers | Possible after demonstrable explanation/correction value | Possible if preparation reduces actual CA back-and-forth |
| Competition | INDmoney/Fold already offer connectors | Free connected dashboards and spreadsheets | Established filing services plus existing CAs |
| Trust | High: financial-data sharing with model providers | High: explain calculations and access first | Very high: private documents and recipient control |
| Technical complexity | High: permissions, grounding, evaluations | High correctness burden, bounded formats manageable | Higher: period rules, package snapshots, revocation |
| Legal complexity | Advice boundaries and processing | Data/consumer duties; descriptive analytics still reviewed | Additional tax wording and professional-role boundaries |
| Retention hypothesis | Novelty may fade | Monthly close/reconciliation could recur | Tax-season use may not recur monthly |
| Acquisition difficulty | Hard to distinguish amid AI products | Demonstrable sample outcome can aid low-cost discovery | Harder explanation and CA trust-building |
| Sustainability hypothesis | Token/support costs without durable advantage | Potential if repeat use covers free subsidy/support | Potential attachment value; professional costs need funding |

Recommend **B as the entry message, C as the expansion journey**, with AI as a supporting explanation tool. “Understand your money, organize financial records and remain prepared for tax season” is comprehensible but broad; it is not yet defensible differentiation.

Proposed wedge: **close one confusing month accurately**. Upload a supported statement, reconcile it, resolve ambiguous transfers/repayments/refunds, and see a source-linked explanation of spending and cash movement with coverage gaps. For incomplete accounts, do not promise total savings. Then reuse reviewed records in a period-specific document checklist and selected CA package. Hypothesized defensibility comes from maintained fixtures, correction/provenance quality and a professionally useful handoff; none exists as a demonstrated moat today.

Show a synthetic-data example before asking for any upload. Let users inspect supported formats and how data is used; make AI optional. Measure export/download effort as part of activation, not only parsing latency. Manual upload is a meaningful disadvantage versus connected alternatives; consent alone does not eliminate that friction. Avoid widening bank coverage or adding alerts to compensate before observing repeat use. The student's budget-alert candidate remains unvalidated and outside this change.

## Startup risk register

Likelihoods below are qualitative **planning hypotheses**, not measured probabilities. Owner roles are proposed; the founder remains accountable until someone is appointed. Security implementation risks remain in [SECURITY](../SECURITY.md).

| Risk | Likelihood hypothesis / impact | Early warning | Mitigation / proposed owner | Evidence still required |
| --- | --- | --- | --- | --- |
| Refusal to upload | High / blocks activation | Demo interest but consent/upload refusal | Sample-first flow, clear access/deletion boundaries / founder | Observed informed choices; reasons for refusal |
| Low willingness to pay | High / no viable revenue | No purchases after useful result | Outcome-first offer; test actual purchases / founder | Paid cohort and alternatives replaced |
| Weak monthly retention | High / low renewal | No next-month import | Measure full recurring effort; seasonal option / product owner | Complete-month cohorts, then actual renewals |
| Free-app competition | High / acquisition pressure | Users prefer connected free dashboards | Demonstrate reconciled month + reusable package / founder | Comparative task evidence |
| PDF maintenance | High / cost and broken imports | Format drift/repeated support tickets | Strict support matrix, fixtures, graceful failure / technical lead | Adapter stability and cost across lawful anonymized fixtures |
| Misclassification | Medium-high / wrong conclusions | Repayments counted as spending | Confidence/review, deterministic totals and provenance / technical lead | Golden fixtures, corrections and independent review |
| AI hallucinations | Medium-high / trust harm | Unsupported answer or missing source | Restricted inputs/queries, citations, refusals / technical lead | Adversarial financial/security evaluations |
| Regulatory changes | Medium / launch rework | New dates/rules contradict copy | Dated source register and pre-release legal review / founder + counsel | Written applicability opinion |
| Sensitive-data breach | Medium / severe harm | Authorization failures, anomalous access | Verify isolation, secure uploads, incident rehearsal / security reviewer | Independent review, recovery and access tests |
| Tax reviewer unavailable | Medium-high / blocks affected tax content | No signed engagement or turnaround | Recruit early; quarantine unreviewed rules / founder | Appointment and period-specific review deliverables |
| Support costs | High / margins erased | Repeated manual import repair | Bounded formats, safe diagnostics, measure minutes / founder | Support distribution including difficult cases |
| Overbuilding | High / schedule/resource loss | Features added before activation evidence | Preserve scope; test weakest assumptions / founder | Reviewable cohort learning, no vanity demand claims |
| Weak differentiation | High / low switching | “My spreadsheet/app already does this” | Observe month-close and CA handoff tasks / product owner | Users choosing and reusing the workflow |
| Brand collision | High / rebrand/legal expense | Confused searches or conflicting mark | Professional clearance before public brand spend / founder + trademark counsel | Registry/phonetic opinion; see [branding](../BRANDING.md) |

## V1 go-to-market proposal

Primary beachhead: employed Indian adults managing multiple bank/card accounts who recently struggled to explain cash movement and collect records for their existing CA. Salary plus occasional freelance income is secondary; complex tax cases receive explicit limits/professional referral, not automated tax advice. Students are not the paying-customer evidence base.

1. Day 5: design a sample-first landing/wireframe flow. Proposed promise: **“Make sense of your monthly money. Keep your tax documents ready.”** Show what is planned versus available; no compliance badges, savings guarantees or “CA-approved” claims.
2. Invite a small, consented early-access cohort through founder/alumni/professional networks and relevant communities with moderator permission. Seek skeptics as well as enthusiasts. Do not scrape contacts, send outreach automatically or collect documents through a waitlist.
3. Only after verified security/privacy gates, let a controlled cohort import supported formats. Observe the complete export-to-review task; collect coarse outcomes, not financial contents. Resolve correctness/trust failures before acquisition expansion.
4. Offer an approved paid plan only after a meaningful reconciled result. Test Plus versus a clearly defined seasonal Tax Pack; don't imply filing is included. [MONETIZATION](../MONETIZATION.md) defines experiments and costs.
5. Test user-initiated referrals after demonstrated value, without exposing financial facts or granting recipient access. Any incentive needs separately approved terms. Trial educational tax-season content only after qualified period review. CA partnerships initially test package usability; no commission or endorsement arrangement is assumed.

| Funnel measure | Cohort/window and denominator | Decision use |
| --- | --- | --- |
| Qualified acquisition | Consenting target-segment signups / unique landing visitors per channel/week; show both counts | Learn channel quality; waitlist interest is not demand |
| Acquisition cost | Cash spend and separately founder recruitment hours / new target-segment signups; later per first payer | Avoid hiding founder effort in “free” acquisition |
| Activation | Existing 7-day reconciled-activation definition in monetization; include upload refusals in signup cohort | Diagnose trust, format access, parsing and correction separately |
| Time to useful result | Median and slow-tail elapsed time from starting statement export to reviewed explanation; failures/cancellations separate | Compare with the person's own workaround, not invented time savings |
| Repeat use | Next-month import / activated users with full next month; also task-based package revisit | Separate monthly users from seasonal users |
| Payment | First successful non-test payer / eligible offer-exposed users, by offer/window | Checkout clicks and survey enthusiasm do not count |
| Refund/support burden | Refunded transactions / settled transactions; support minutes per active and paid user | Inspect dissatisfaction and contribution margin |
| Retention | Next-month reuse and eligible annual renewal, reported separately | Annual renewal cannot be proven during the build schedule |

Before increasing marketing spend, require a founder-reviewed cohort showing accurate reconciled outcomes, comprehensible limitations, voluntary paid use, repeat usage appropriate to the offer and measured contribution after free-user subsidy/support. Predeclare cohort sizes, observation windows, loss budget and stop rules; no numerical conversion benchmark is invented here. Pause real-data expansion for unresolved security or financial correctness failures regardless of growth. Good documentation permits Day 5 design, not a launch or a pricing-validation claim.

## Follow-ups and handoff

Pending founder decisions D4-01–D4-07 are in [DECISIONS](../DECISIONS.md). [SCREENS](../SCREENS.md) contains the Day 5 handoff; [REGULATORY_REVIEW](../REGULATORY_REVIEW.md) and [BRANDING](../BRANDING.md) contain review blockers. No new GitHub issues, source IDs or release assignments were created.

### Validation record

Executed on 2026-10-11:

| Check | Actual result / scope |
| --- | --- |
| `python -X utf8 scripts/validate_manifest.py` | PASS: 194 features, 85 working days |
| `python -X utf8 -m unittest discover -s tests -v` | First sandbox run: 5 passed, 1 temporary-directory PermissionError. Authorized rerun outside sandbox: **6/6 passed**, 0 failures/errors; no test or tracker edits |
| Local Markdown links, ad hoc Python check | PASS: 191 relative/local links across 29 Markdown files, including 1 heading fragment; 0 missing targets. This is not an external HTTP or authenticated-page validation |
| Feature/release and daily-ID assertions | PASS: 194 unique feature IDs; V1 140, V1.5 14, V2 20, V3+ 8, Future 12; 85 unique daily IDs |
| `git diff --check` | PASS; Git emitted existing Windows LF-to-CRLF conversion notices, not whitespace errors. New untracked Markdown also checked separately for trailing whitespace/conflict markers |
| Protected-path comparison against HEAD | PASS: manifests, brand config, scripts, workflows, tracking sheets and generated documents unchanged |
| Commercial scenario arithmetic | Decimal calculations produced the displayed results; hypothetical inputs are not validated business evidence |

Tracked-file diffs and both new documents were reviewed. No application code changed; no application lint/type/financial-fixture suite exists to exercise here, and no security, legal or tax-professional test result is claimed. Live Issue #12 inspection failed due to TLS timeout; trademark results require authenticated search and some official documents need follow-up retrieval. No commit, push, issue change, closure or verified label. DAY-004 is ready for founder review of this desk-research draft, not automatically verified; FIN-004 tested pricing remains pending.

# FINNest — DAY-002 assumption and evidence register

**Task:** [DAY-002 / Issue #10](https://github.com/Tejanshu22/PersonalFinanceManager/issues/10). **Status: founder-approved survey-only DAY-002 scope; closeout awaiting final acceptance and publication.** Documented usable interviews: **0/5**. The owner supplied an anonymized report of five actual Google Form submissions on 2026-10-11: two salaried employees, one salaried employee with freelance income, and two students. The three employed respondents form the target subgroup; students provide auxiliary feedback. The founder has replaced the Day 2 five-interview gate with this limited exploratory survey pilot. Five future interviews are a separate nonblocking follow-up; no interviews are claimed and FIN-002 still requires at least ten actual interviews. See [revised closeout criteria](research/DAY_02_CLOSEOUT.md).

Use the [guide](DAY_02_INTERVIEW_GUIDE.md) and [P01–P05 notes](DAY_02_INTERVIEW_NOTES.md). Read [requirements](REQUIREMENTS.md), [pricing hypotheses](MONETIZATION.md) and [open decisions](DECISIONS.md) for the existing scope. This register may recommend later changes, but cannot change release classifications, priorities or acceptance criteria in the manifests.

## Source and evidence boundary

Source: [anonymized survey pilot report](research/DAY_02_SURVEY_PILOT.md), prepared 2026-10-11. Raw Forms rows, identities, original question wording/options and consent records were not independently inspected. The archive records source provenance and preserves the report's recommendations as proposals. Only this supplied aggregate report was added; no raw responses, recordings or financial records were copied.

Evidence references below identify report sections, not individual people or interview statements. **Reported survey evidence** is attributed self-report; **interpretation** is the researcher's inference; **untested** means behavior, severity or value has not been established. No new direct participant quotation is asserted. P01–P05 remain interview slots and are not aliases for these survey respondents.

| Ref | Source location | Evidence type / boundary |
| --- | --- | --- |
| SP-01 | Report §1 | Sample composition, convenience sampling and response-quality limitations |
| SP-02 | Report §2, Q08 | Prompted multiple-choice problem selections; not measured incident frequency or severity |
| SP-03 | Report §3 | Employed tax difficulties and contradictory straightforward-filing response |
| SP-04 | Report §4, Q13 | Prompted upload/privacy barriers, separately reported for all five and employed three |
| SP-05 | Report §4, Q14 | Prompted safeguard preferences; not observed control effectiveness |
| SP-06 | Report §5, Q15 | Single preferred hypothetical capability |
| SP-07 | Report §5, Q16 | Hypothetical first prototype action; no upload observed |
| SP-08 | Report §5, Q17 | Hypothetical annual-price bands; no purchase observed |
| SP-09 | Report §5, Q18 | One student's unprompted budgeting suggestion, as summarized by the report |

This is a small self-selected convenience sample, not market prevalence or conversion evidence. Counts use the stated denominator; multiple selections can overlap. Do not combine employed and student responses to validate the salaried persona. No individual cross-question linkage or separate salaried-plus-freelance conclusion is inferred from the aggregate report.

## Assumption-validation matrix

Supporting and challenging signals remain prospective interview coding guidance. Current status uses only the attributed pilot evidence; no assumption is marked validated. Question IDs refer to the interview guide, not the survey numbering. Feature mappings identify existing relevant backlog items, not priority changes.

| Ref | Assumption / existing IDs | Questions | Evidence that could support it | Evidence that could challenge it | Current status / references |
| --- | --- | --- | --- | --- | --- |
| A01 | Multi-account fragmentation creates meaningful recurring effort; FIN-012, FIN-053 | Q01–Q04 | A recent concrete reconciliation problem, repeated effort and an inadequate workaround | Few accounts, clear understanding, or a reliable effortless existing process | Preliminary support for reported fragmentation: 2/3 employed selected combining accounts/cards (SP-02); recurring effort and workaround remain untested |
| A02 | Separating purchases, repayments, transfers and savings helps users understand changes; FIN-040, FIN-042, FIN-048, FIN-064 | Q02, Q04, concept | Participant independently describes unexplained totals/double counting and a consequential workaround | No confusion; issue is income variability or behavior that this tool cannot address | Preliminary support for reported confusion: 3/3 employed selected descriptions/transfers (SP-02); double counting, savings comprehension and solution accuracy untested |
| A03 | Organizing tax documents is a significant job distinct from filing; FIN-077, FIN-081, FIN-090 | Q05–Q06 | Recent searching, missing records, repeated CA requests or preparation delay | Records already organized; the only need is tax computation or filing outside V1 | Preliminary support for uncertainty: 3/3 employed reporting difficulty, 2/3 what to send CA (SP-03); actual delay/severity mixed or unknown |
| A04 | Some target users will consider uploading statements under understandable trust conditions; FIN-017, FIN-023, FIN-115 | Q08, concept | Specific conditions and willingness to consider manual upload after limitations are understood | Firm refusal, requirement for an unoffered local-only option, or unacceptable privacy tradeoff | Mixed hypothetical evidence: 2/3 employed would try a statement after privacy review, 1/3 would wait (SP-07); 0/3 selected blanket refusal (SP-04), not proof of upload |
| A05 | Manual upload/reconciliation/correction effort is acceptable compared with current work; FIN-029, FIN-038, FIN-046 | Q01, Q07, concept | Existing manual effort and a credible preferred workflow, including tolerated corrections | Upload/review is more burdensome or only automatic bank feeds would be acceptable | Concern challenges acceptable-effort assumption: 3/3 employed selected regular-upload effort (SP-04); acceptable cadence/correction burden untested |
| A06 | Financial summaries/recurring insights can motivate monthly use; FIN-059, FIN-065 | Q01–Q02, Q09 | A recurring decision tied to a monthly event or repeated charge review | Seasonal-only need or no reason to return; reminders alone do not prove demand | Inconclusive: 2/3 employed prefer recurring/unusual detection, 1/3 reports (SP-06); no repeat-use evidence |
| A07 | Grounded financial questions add value beyond reports; FIN-068–076 | Q09, concept follow-up only if relevant | A specific unresolved question tied to a real workflow and acceptable AI boundaries | Reports already suffice, questions are outside scope, or AI processing is unacceptable | Inconclusive: only one student chose natural-language questions as top feature (SP-06); no employed top choice does not establish no value |
| A08 | Selected CA document sharing is useful and trusted; FIN-090–096 | Q05–Q06, Q08, concept | Existing repeated sharing pain and a need for scoped access/history | Existing sharing is sufficient or downloaded-copy limitations make the proposal unsuitable | Preliminary trust signal: 3/3 employed selected revocable CA access (SP-05); 2/3 unsure what to send (SP-03); sharing workflow and CA value untested |
| A09 | Plus at ₹999/year could fit sustained individual value; FIN-097, FIN-106 | Q09–Q10, pricing | Relevant past payments plus a specific recurring job and tradeoff rationale | No recurring job, satisfied free alternative, annual price/value mismatch | Inconclusive: employed annual bands split across three ranges (SP-08); no actual purchase or recurring-value validation |
| A10 | ₹499 Tax Pack can create seasonal value without tax filing; FIN-081, FIN-090, FIN-097 | Q05–Q06, Q10, pricing | Clear value placed on preparation alone and understandable purchase unit | Participant expects filing, dislikes separate charging, or preparation alone is not worth paying for | Untested: annual-price bands do not test a one-time preparation-only pack (SP-08) |
| A11 | Salaried people with supplementary income fit the bounded V1; FIN-013, FIN-048, FIN-081 | Q01–Q02, Q05–Q06 | Personal income organization is the actual job | Need centers on invoicing, GST, bookkeeping or complex tax beyond V1 | Untested: one salary-plus-freelance respondent present (SP-01), without isolated workflow evidence |
| A12 | Existing alternatives leave a problem worth switching for; FIN-002, FIN-004 | Q01, Q07, Q10 | Specific unmet job and switching effort the participant can explain | Current app/spreadsheet/CA works well; startup trust and habit costs outweigh proposed value | Untested: no usable tool-performance/switching evidence in supplied summary; contradictory paid-service answer needs clarification (SP-01) |

Interviews can test perceived usefulness and stated concerns. They cannot prove financial accuracy, production security, legal compliance, tax correctness, actual retention or actual conversion. External professional-review gates remain unchanged.

## Participant coverage ledger

These are interview slots, not the five survey respondents. Recruitment/attendance is not inferred from a filled ID. No survey response is counted as a completed interview.

| Participant | Genuine notes received | Consent/privacy review | Usable completed interview counted | Missing evidence |
| --- | --- | --- | --- | --- |
| P01 | No | Pending | No | All participant responses |
| P02 | No | Pending | No | All participant responses |
| P03 | No | Pending | No | All participant responses |
| P04 | No | Pending | No | All participant responses |
| P05 | No | Pending | No | All participant responses |

## Analysis protocol once real interview responses arrive

1. Confirm source participant, distinctness, actual interview, consent scope and privacy review; ask for clarification where missing. Do not infer consent from receipt of notes. Do not seek financial documents to corroborate stories.
2. Classify each entry using S/O/I/U from the notes template. “Verified participant statement” means traceable to the supplied real interview record and faithful to the speaker; the underlying claim remains self-reported unless separately evidenced.
3. Separate problems described before the concept from prompted reactions. Tag hypothetical price choices separately from past purchasing. Record the offered wording, topic gaps and any meaningful researcher influence.
4. Code actual examples, frequency, severity, workaround and voluntary approximate costs. Keep “not asked,” “unclear,” “not applicable” and “declined” distinct from “no problem.” Do not assign severity or financial cost without evidence.
5. Link every synthesis claim to stable evidence IDs, such as P01-E01. Keep supporting and contrary evidence and differing segments visible. Distinct people, not number of quotes, determine repetition counts.
6. Describe patterns as n of the participants actually asked/responding, with denominators and gaps. Five interviews are qualitative directional evidence, not market size, statistical prevalence or a conversion-rate estimate. One serious objection can matter without majority support.
7. For each assumption, use Untested, Inconclusive, Supported in this sample, Challenged in this sample or Mixed. Explain evidence and uncertainty; do not turn positive product reactions into validated demand. No numeric approval score or majority-vote product decision is assumed.
8. Final interview recommendations wait for genuine notes; preliminary survey interpretations must remain separately attributed and qualified. Distinguish owner decisions from researcher recommendations. Update open questions and propose targeted Day 3 follow-ups. Obtain explicit approval before any source-manifest or scope change.

## Preliminary pain points and financial-accuracy implications

| Reported survey evidence | Reference | Researcher interpretation | Missing evidence / counter-signal |
| --- | --- | --- | --- |
| Confusing descriptions/transfers: 3/5 overall, 3/3 employed; combining accounts/cards: 2/5, 2/3 | SP-02 | Explore source-linked reconciliation and comprehension within the existing financial contract | Actual incident, consequences, workaround and recurring cost not supplied |
| Unknown spending: 4/5 overall, 2/3 employed; estimating remaining money: 3/5, 2/3 | SP-02 | Test whether qualified spending/cash-flow views explain a real decision | Does not prove users need the same metric; income less consumption is not available cash |
| Unclear recurring charges: 2/5 overall, 2/3 employed; unexpected/possible duplicates: 1/5, 1/3 | SP-02 | Explore why recurring/unusual review could prompt a return | No confirmed duplicate, fraud event, measured loss or retention evidence |
| Inaccurate categories/insights concern: 2/5 overall, 2/3 employed | SP-04 | Test comprehension of provenance, corrections and incomplete-data warnings | Concern is not a failed product test or proof that proposed calculations are correct |
| Reporting income/investments unclear: 3/3 employed; reconciling tax records, what to send CA and tax changes: 2/3 each | SP-03 | Test readiness checklist and CA-package usefulness within V1 | Students had not filed and are excluded from the employed denominator; one employed respondent also found filing straightforward |

No voluntary time/cost estimates or incident-level severity were supplied. Some recent-incident answers reported no recent difficulty despite selecting problem categories (SP-01). Multiple-choice selection does not establish frequent or costly pain. Preserve deterministic calculations and distinctions among income, consumption, investments, transfers, card purchases/repayments, refunds/reversals, cash flow and qualified savings from [requirements](REQUIREMENTS.md). Customer concern neither verifies nor relaxes the correctness contract. Tax-readiness signals do not authorize tax calculations, filing or unreviewed tax advice; [professional review](TAX_POLICY.md) remains pending.

## Current tools and competitor insights

No usable tool-specific performance, workaround, switching or abandonment evidence is included in the aggregate report. One respondent selected both a paid personal-finance/budgeting app and “None of these” in Q12 (SP-01); their subgroup is unspecified. Do not infer a clean nonpayment count, identify them, drop their other responses or resolve the conflict without clarification. Ask about actual past services and outcomes. No competitor capabilities, prices or market claims were researched or established here.

## Trust, privacy and upload friction

| Reported selection | All respondents | Employed subgroup | Reference |
| --- | --- | --- | --- |
| Unclear who views statements | 5/5 | 3/3 | SP-04 |
| Breach concerns | 4/5 | 2/3 | SP-04 |
| Regular-upload effort | 4/5 | 3/3 | SP-04 |
| Advertising/data-sale concern | 3/5 | 2/3 | SP-04 |
| Refusal of any third-party upload | 2/5 | 0/3 | SP-04 |
| Retention/deletion unclear | 2/5 | 2/3 | SP-04 |
| Inaccurate categories/insights | 2/5 | 2/3 | SP-04 |

Privacy/deletion transparency, sample/redacted trial, independent security assessment and revocable CA access were each selected by 4/5 overall (SP-05). Independent assessment and CA revocation were each selected by 3/3 employed; employed counts for the other two safeguards are not supplied. These are prompted preferences, not evidence that controls exist or overcome objections.

Hypothetical first action (SP-07): two employed respondents would try one real statement after privacy review; the third would read more and await reviews. Both students preferred sample/redacted data. Blanket third-party refusal was reported only in the student subgroup; it remains a useful objection to explore, not a salaried refusal rate. Do not infer that the employed participants consented to uploads or that student trial interest would convert into real uploads.

**Interpretation:** explain owner, CA, support and AI access separately; clarify retention/deletion and downloaded-copy revocation limits; explore retrieval/re-upload effort, supported-format clarity and stale/partial-data comprehension. These reinforce existing trust requirements rather than approve new infrastructure. No independent audit or security verification is claimed. Any proposed demo uses synthetic examples; no customer statements, credentials, PAN, account numbers, salary amounts or financial screenshots are requested. [Real-data safeguards](SECURITY.md) and research consent arrangements remain gates, regardless of hypothetical willingness.

## Pricing feedback — hypothetical, unchanged offers

| Reported annual choice (SP-08) | Employed n=3 | Students n=2 | Interpretation limit |
| --- | --- | --- | --- |
| Up to ₹499 | 1 | 0 | Annual band, not the one-time Tax Pack |
| ₹500–₹999 | 1 | 0 | Does not establish purchase at the top of the band |
| ₹1,000–₹1,999 | 1 | 0 | Does not validate an advanced-tax product or its entitlements |
| Uncertain until trial | 0 | 2 | Trial preference is not conversion |

No working-service use or purchase occurred as part of this survey, according to the report. The exact original questionnaire wording was not independently reviewed. Free ₹0, Plus ₹999/year, one-time Tax Pack ₹499 and later advanced-tax ₹1,999/year remain the [existing hypotheses](MONETIZATION.md); no price, entitlement or release change follows. Actual prior spending, value rationale, recurring versus seasonal need and switching cost require interviews. No conversion, revenue, optimum price or market demand is inferred.

## Feature-priority evidence — research follow-ups only

Single preferred hypothetical capability (SP-06): reports 2/5 (one employed, one student), recurring/unusual detection 2/5 (both employed), natural-language questions 1/5 (student). This constrained choice does not measure absolute demand or justify removing AI, changing priorities or promoting deferred features.

| Existing IDs / candidate | Evidence / proposed research follow-up | Boundary / owner decision |
| --- | --- | --- |
| FIN-040, FIN-042, FIN-048, FIN-053, FIN-064: reconciled financial clarity | SP-02/SP-04; examine real confusion and, later, synthetic report comprehension | Existing scope and accuracy rules retained; no implementation evidence |
| FIN-017, FIN-023, FIN-029, FIN-038, FIN-046, FIN-115: trust and import effort | SP-04/SP-05/SP-07; explore permissions explanation and actual retrieval/correction burden | No new adapter, reminder or sync capability approved |
| FIN-059, FIN-065: reporting and recurring insights | SP-06; establish an actual recurring decision and revisit trigger | Hypothetical preference is not retention; no feature priority change |
| FIN-077, FIN-081, FIN-090–096: readiness and selected CA sharing | SP-03/SP-05; establish preparation pain and CA package requirements | Not filing, tax computation or a CA workspace; qualified review remains necessary |
| FIN-068–076: grounded financial questions | SP-06; test added value after unaided problem discovery | Inconclusive for salaried users; no removal or scope expansion |
| CAND-D2-01: budget-threshold alerts and adaptive budget suggestion | SP-09; one student suggestion. Ask whether employed users already budget, which thresholds matter and what they do when exceeded | **Unvalidated research candidate**, not a new FIN ID or release assignment. Related FIN-147 remains V1.5; alerts/adaptive behavior are not silently added to its acceptance |

The report's P0/P1/P2 recommendations are the author's proposals, not authoritative backlog priorities. FIN-027, FIN-063, FIN-066 and FIN-067 remain V1.5. No source-manifest changes are authorized by this integration. Security and financial correctness cannot be removed by customer preference.

## Outstanding interview questions and Day 3 follow-ups

Ask about current behavior first, without announcing survey results or suggesting expected answers. These are optional probes within the [existing guide](DAY_02_INTERVIEW_GUIDE.md), not additional mandatory questions that extend every session:

1. What was the last confusing financial entry or monthly total, if any? What did you do next? Did it cause a decision, delay or loss of time? If there was no difficulty, what worked well?
2. Walk through the steps you normally take to retrieve and review statements, without opening or sending them. How often do you do it, and where does the effort arise? What correction effort would outweigh the benefit?
3. What would you need to know before considering an upload, and what would still make you decline? After spontaneous concerns, probe CA/support/AI access, deletion, independent-review evidence and revocation limits separately.
4. Describe your most recent tax preparation. What was unclear, what was straightforward, and did uncertainty actually delay anything? Which documents did you need to find or send? No documents are requested.
5. What financial-management or tax service have you actually paid for, if any? What job did it do and why was it worth paying for? Approximate service cost is optional; no receipt, salary or account details are needed. Clarify contradictory paid-service selections only with a legitimate participant connection.
6. What would prompt another review of finances next month? What do you do about recurring or unusual charges today? Reports and AI reactions should be explored after concrete problems, not treated as forced either/or demand.
7. What would make a preparation-only Tax Pack useful separately from filing? Would annual use or seasonal use fit the job? Show unchanged pricing hypotheses only near the end; record rationale and refusal equally.
8. How do you set or review budgets today, if at all? When a limit is exceeded, what action follows? Discuss the alert/adaptive-budget concept only after current behavior; do not introduce it as an approved capability.
9. What do current apps, spreadsheets, bank tools or CA services already solve well? What would justify switching? For salary-plus-freelance users, does the unmet job stay within personal organization or require excluded bookkeeping/GST work?

Schedule the five distinct target-customer interviews as a nonblocking follow-up, including skeptics and satisfied-tool users where possible; do not fill slots with student survey submissions or a CA consultation. Refine Day 3's existing five-more-prospects and two-CA agenda from actual notes and sampling gaps. CA follow-ups concern package completeness, source/coverage information, permissions and downloaded-copy limits; they do not replace qualified tax review or require client files. No Day 3 sessions or outreach are started by this integration.

The report suggests expanding to 15–25 survey responses. That is an optional research proposal requiring an owner decision about value and capacity, not an added Day 2 acceptance gate or a substitute for interviews.

## Current outcome and review gate

The pilot supports asking more precise questions about financial clarity, trust, upload friction and tax preparation. Interpretation remains preliminary; the study does not establish severity, viable pricing, retention, solution effectiveness, compliance or security. Dissent and contradictions remain visible, and the salaried-plus-freelance persona cannot be independently assessed from one unsegmented response.

Remaining DAY-002 requirements: record the superseding acceptance on Issue #10, create/link the nonblocking interview follow-up, validate the documentation, obtain final owner acceptance and confirmation to commit/push, then satisfy repository verification gates before authorized closure. Five interviews are no longer a Day 2 gate. FIN-002 remains open/unverified under its unchanged ten-interview requirement. No feature releases, pricing or generated progress files change. See [open decisions](DECISIONS.md) for research arrangements, candidate handling and professional-review dependencies.

## Prior survey-integration validation — 2026-10-11 (historical)

These historical checks cover the earlier seven-file survey integration. Current closeout checks are recorded in [DAY_02_CLOSEOUT](research/DAY_02_CLOSEOUT.md). They do not verify underlying respondent claims, customer demand or production controls.

| Check | Actual result |
| --- | --- |
| `python scripts/validate_manifest.py` | PASS: 194 features, 85 working days |
| `python -m unittest discover -s tests -v` | Initial sandbox run: 5 passed, 1 temporary-directory PermissionError. Authorized run outside sandbox: all 6 passed, no failures/errors |
| Local Markdown checks | PASS: 117 local links and 1 heading fragment across 23 Markdown files; UTF-8 decoding and fence balance checked. External URLs not fetched |
| Whitespace | PASS: `git diff --check` plus explicit checks including the new untracked report. Git emitted LF-to-CRLF conversion notices, not whitespace errors |
| Report fidelity | PASS: archived report matches the supplied source apart from declared trailing-whitespace/newline normalization; original file SHA-256 recorded |
| Research evidence boundary | PASS: five blank interview templates and 50 evidence slots unchanged; 12 assumption IDs retained; documented interviews remain 0/5 |
| Scope preservation | PASS: exactly seven authored Markdown files changed/added on master; pricing table unchanged; no source-manifest, generated-artifact, configuration, workflow or application-code changes |
| Feature IDs/releases | PASS: 194 unique IDs; V1 140, V1.5 14, V2 20, V3+ 8, Future 12 |

No bootstrap or live synchronization was run. The existing tracker test generates isolated temporary fixtures only. No application or financial-fixture results, professional reviews, fresh GitHub status checks or interview completion are claimed.

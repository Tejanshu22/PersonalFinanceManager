> Repository evidence note — founder-approved DAY-002 acceptance amendment, 2026-10-11.
> The supplied revised aggregate report supersedes the previous report's interview gate, not its research counts. Scope acceptance is approved; final verification, commit/push and issue closure remain pending. No interviews, demand, purchases, security audit or consent records are independently verified by this report.
> Source: `FINNest_Day2_Closeout_Patch/docs/research/DAY_02_SURVEY_PILOT.md`; SHA-256: `31b0e40ab6a70dff1ee9cdf8e11626d05ca331cd62c6e5be8c2dd9e9d6034891`. Previous source SHA-256: `89efdafe18fc4851168ac1caa5328aa18d8cd88fee080cc0cf5a8539e2637882`. Text below is preserved apart from trailing-whitespace/newline normalization.
> Source recommendations are not automatic authority for GitHub actions, pricing or feature changes. The five future customer interviews remain separate from CA discovery; no CA consultation substitutes for a target-user interview. See [closeout criteria](DAY_02_CLOSEOUT.md) and [decision log](../DECISIONS.md).

# FINNest — Day 2 Survey Pilot Findings

**Research stage:** Five-response survey pilot; accepted as the revised, limited Day 2 deliverable. Full customer discovery remains pending.
**Source:** FINNest Day 2 Google Form response export, 5 voluntary responses
**Prepared:** 2026-10-11
**Data handling:** This report contains only aggregated or generalized responses. Do not commit the raw respondent export to a public repository.

## 1. Sample and limitations

- **N = 5**: 2 salaried employees, 1 salaried employee with freelance income, and 2 students.
- **Target-audience subgroup = 3 employed respondents**. The student responses are useful for general usability but should not determine the salaried-professional roadmap.
- Self-selected convenience sample. Not a representative study; respondents' statements are self-reported.
- This is a survey, **not five live interviews**. Under the founder-approved Day 2 scope change, the pilot may satisfy the revised DAY-002 acceptance criteria after review and repository evidence. Full interviews remain a separate open research task.
- One respondent selected **both “Personal-finance or budgeting app” and “None of these”** for paid services in Q12. Do not use the raw “None” total as a clean nonpayment statistic.
- Some responses to the most recent incident question were “No” or “No recent difficulty,” while participants selected current problem categories; follow-up examples are needed to establish severity.
- Pricing question measures hypothetical consideration, **not actual transactions or conversion**.

## 2. Problem frequency

| Recent problem (Q08; multiple selections allowed) | All respondents (n=5) | Employed subgroup (n=3) |
|---|---:|---:|
| Not knowing where money was spent | 4 | 2 |
| Confusing descriptions or transfers | 3 | **3** |
| Difficulty estimating remaining money | 3 | 2 |
| Difficulty combining accounts/cards | 2 | 2 |
| Unclear subscriptions/recurring charges | 2 | 2 |
| Unexpected/potentially duplicate charges | 1 | 1 |

**Interpretation:** The clearest hypothesis to test is whether FINNest can generate **reconciled, understandable reports across accounts and cards**. Do not replace accurate calculations with AI storytelling.

## 3. Tax-readiness signal

- All **3/3 employed respondents** selected difficulty understanding which income or investments must be reported.
- **2/3 employed respondents** selected reconciling tax records; **2/3** selected uncertainty about what to send a CA; **2/3** selected tax-rule changes.
- Two respondents were students who had not filed tax returns; they should not dilute the employed-person tax signal.
- One employed respondent simultaneously selected “Filing was straightforward” and a tax-understanding difficulty, which may mean some uncertainty did not actually prevent filing.

**Interpretation:** Continue prioritizing tax-document readiness and CA-ready export as a differentiator, without building unverified tax calculations into V1.

## 4. Trust and upload barriers

| Barrier (Q13; multiple selections) | All n=5 | Employed n=3 |
|---|---:|---:|
| Unclear who can view statements | **5** | **3** |
| Data breach concerns | 4 | 2 |
| Effort to upload regularly | 4 | **3** |
| Sale/use of data for advertising | 3 | 2 |
| Refusal to upload to any third-party app | 2 | 0 |
| Unclear retention/deletion | 2 | 2 |
| Inaccurate categories/financial insights | 2 | 2 |

Safeguards selected most often (Q14): **privacy/deletion transparency, sample/redacted-data trial, independent security assessment, and revocable CA access (4/5 each)**. Independent security assessment and CA revocation each received **3/3 in the employed subgroup**.

**Interpretation:** Prioritize a transparent permissions/retention explanation, clear data-freshness labeling, and a synthetic/redacted demonstration. Don't claim a security audit exists until independently performed. A “no bank credentials requested” guarantee should be prominent.

## 5. Concept, usage and pricing

### Preferred single feature (Q15)
- Combined income/spending reports: **2/5** (1 employed)
- Recurring/unusual charge detection: **2/5** (2 employed)
- Ask questions in ordinary language: **1/5** (student)

### Prototype first action (Q16)
- Sample/redacted data: **2/5** (both students)
- One real statement after privacy review: **2/5** (both employed)
- Read more and wait for reviews: **1/5** (employed)

### Hypothetical annual price (Q17)
- Uncertain until trial: **2/5** (both students)
- Up to ₹499: **1/5** (employed)
- ₹500–₹999: **1/5** (employed)
- ₹1,000–₹1,999: **1/5** (employed)

**Interpretation:** ₹999/year remains an experiment, not a validated price. Do not infer that 3/3 employed respondents will pay: no one has purchased or used the working service as part of this survey.

### Unprompted feature request (Q18)
One student suggested **budget threshold alerts and an adaptive budget informed by past spending**. Record as a potential future feature, not yet sufficient evidence to reprioritize the V1 roadmap.

## 6. Recommended actions (prioritized, not yet approved scope changes)

| Priority | Recommendation | Linked signal | Follow-up |
|---|---|---|---|
| P0 | Keep source-reconciled money dashboard / classification as the initial core | 3/3 employed cite confusing transaction descriptions/transfers | Test with realistic synthetic examples |
| P0 | Show data access, privacy, retention/deletion, and permissions before upload | 5/5 unclear who views statements | Usability test with trust walkthrough |
| P0 | Build sample/redacted-data demo and supported-format clarity | 2 students want sample first; 3/3 employed say upload effort is a barrier | Test demo-to-real-import funnel |
| P0 | Explain partial data, calculation sources and user corrections | 2/3 employed worry about inaccurate insights | Ask interviewees to verify dashboard screenshots |
| P1 | Keep tax readiness / CA-ready package in the release hypothesis | 3/3 employed have reporting uncertainty | Interview employed users and CAs about actual workflow |
| P1 | Keep basic recurring/unusual charge detection in V1 | 2/3 employed pick this as top feature | Test whether they would revisit monthly |
| P2 | Consider budgeting/threshold alerts after evidence | One student suggestion | Record as candidate for post-V1, do not change manifest |
| P0 | Validate actual willingness to pay | Price answers hypothetical and split | Ask for waitlist/paid pilot only after ethical, safe product readiness |

## 7. Next interviews: questions that the survey cannot settle

1. **Recent concrete incident:** “Walk me through the last time a transfer, card charge or monthly balance confused you. What did you do next?”
2. **Effort:** “What exact steps do you take to retrieve your statement? Would you repeat them every month?”
3. **Trust:** “What would you need to see on the upload screen to feel safe—and what wouldn't change your mind?”
4. **Paid status clarification:** “Have you actually paid for a budgeting app, tax filing service or CA in the last year?” (Do not collect identifying account details.)
5. **Tax readiness:** “Which documents were missing, and how much time did gathering them take?”
6. **Purchase behavior:** “Have you paid for a solution to this specific problem? What was the trigger and amount?” Avoid treating price-band selection as purchase intent.
7. **Value proposition comparison:** Show a mock reconciled dashboard, anomaly check and tax checklist; ask which one solves a problem they had recently.
8. **Budgeting request:** For those interested in budget alerts, determine whether they already set budgets or only prefer the concept.

## 8. Revised Day 2 acceptance and GitHub tracking

The founder has authorized a **scope adjustment**: DAY-002 will be accepted as a five-response survey pilot so development can proceed. This **replaces the interview deliverable for the Day 2 milestone only**; it does not mean the five interviews happened or that customer demand is validated.

- Save this anonymized report under `docs/research/DAY_02_SURVEY_PILOT.md` and link it in DAY-002 (GitHub Issue #10).
- Record the approval to accept survey-only Day 2 evidence in `docs/DECISIONS.md` and update Issue #10's acceptance criteria or append a clearly labeled superseding acceptance comment **before** closure.
- Create a separately tracked, nonblocking follow-up issue for five qualitative customer interviews, ideally including three or more salaried professionals. Link it from Issue #10.
- FIN-002, **Customer discovery interviews**, must remain unverified if its acceptance criteria require real interviews. Do not use survey responses to close it.
- Revalidate documents and tracker scripts. After human acceptance, commit/push the research documentation, label Issue #10 `verified`, and close it. Then allow GitHub Actions to update generated progress files.
- Maintain approved V1 feature classifications; this survey does not justify reprioritizing features yet.
- Keep raw Google Sheet and raw XLSX **private and out of GitHub**.

## 9. Suggested next evidence target

Collect **15–25 varied survey responses** for additional directional patterns, with priority given to employed users rather than students; complete **five real 15–20 minute interviews**, including employed respondents and ideally a CA consultation. Do not treat a convenience sample as representative, regardless of its size.

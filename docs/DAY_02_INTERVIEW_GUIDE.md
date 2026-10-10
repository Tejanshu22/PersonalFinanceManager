# FINNest — DAY-002 customer interview guide

**Task:** [DAY-002 / Issue #10](https://github.com/Tejanshu22/PersonalFinanceManager/issues/10). **Stage:** research preparation; no participant responses supplied. **Session length:** 15–20 minutes. This operational guide supersedes the longer interview outline in [Day 1 preparation](DAY_01_KICKOFF.md).

Use the [five participant templates](DAY_02_INTERVIEW_NOTES.md) and [assumption/evidence register](DAY_02_RESEARCH_SUMMARY.md). Product boundaries and prices come from [requirements](REQUIREMENTS.md) and [monetization](MONETIZATION.md); they remain hypotheses where marked. No application, architecture, manifest, generated-tracker or GitHub-state changes are part of this research preparation.

## Research objective and evidence boundary

Understand whether the target users experience sufficiently important financial-organization problems, how they solve them now, what prevents statement uploads, and what could justify repeat use or payment. Discover reasons **not** to build or prioritize a capability as well as reasons to pursue it. A prepared guide is not an interview; an enthusiastic reaction is not a purchase.

DAY-002 requires five distinct real participants and a reviewed synthesis. FIN-002 requires at least ten interviews across the wider discovery effort; the Day 2 five contribute to that requirement without completing it. Day 3 additionally plans five more prospects and two CAs under the existing roadmap. No research results or completion labels are inferred from the current generated tracker. The local roadmap links DAY-002 to #10; the live read of #10 timed out, so its latest body/labels could not be confirmed.

## Recruit five people for relevant experience, not agreement

Target Indian salaried professionals approximately 23–40 who manage some combination of monthly spending, bank/card accounts, investments or annual tax documents. Self-described broad fit is enough; do not collect proof of age, employment or financial holdings. Include salary plus supplementary income where feasible, without presenting bookkeeping or advanced tax as V1 capabilities.

Suggested mix, not participant facts or mandatory quotas:

| Sampling dimension | Recruitment aim |
| --- | --- |
| Financial responsibility | People who personally review spending or gather their tax records; not only those whose affairs are handled entirely by someone else |
| Complexity | Include multi-account/card users and at least one simpler-account user to test whether complexity predicts pain |
| Existing workaround | Seek both spreadsheet/app users and people relying on bank apps, memory or a CA |
| Confidence and skepticism | Include people satisfied with current tools or reluctant to upload documents; do not select only FINNest enthusiasts |
| Income mix | If available, include a salaried person with supplementary freelance/other income; record a sampling gap if unavailable |
| Independence | Avoid five people from the same household/team or only close friends; describe recruitment bias without recording identifiable relationships |

Recruit through the owner's personal/professional network and permitted community channels. The owner sends invitations; this task does not authorize automated outreach or messages. Keep scheduling contacts and any P01–P05 identity mapping in approved private storage outside Git. Count a person once, even if interviewed twice. If someone declines or stops, retain only permitted non-identifying process notes and recruit another distinct participant; do not invent a replacement or renumber existing evidence silently.

Optional invitation for the owner to use: “I'm researching how salaried people manage everyday finances and tax paperwork. Could we speak for 15–20 minutes about your current process? This is not a sales call. No statements, salary details or financial identifiers are needed. You can skip questions or decline.”

Reserve five 20-minute sessions plus approximately 10 minutes after each for permitted note cleanup: about 2.5 hours, excluding recruitment. Schedule a separate 45–60 minute synthesis after real responses arrive. These are planning estimates, not completed work. No incentive is assumed; if one is proposed, approve its amount/terms first and disclose it independently of answers.

## Before collecting notes

The owner must choose an approved private notes location, who may access it, a retention/deletion period, a withdrawal channel and the intended sharing/AI-analysis scope. These are open research decisions, not assumed resolved by the product's future privacy controls. Until agreed, do not collect interview notes. Blank templates can be prepared now.

- Default to **no recording**. Declining recording must not prevent participation. Do not enable transcription or meeting assistants without separate explicit consent and an approved storage/processor arrangement.
- Obtain permission for minimal de-identified notes. Separately explain and obtain permission before excerpts are placed in repository documentation, quoted, or supplied to Astra/other analysis services. Participation consent is not marketing, upload or AI consent.
- Do not request bank statements, tax forms, credentials, PAN, account/card numbers, passwords, salary amounts, balances, client records or screen sharing of financial apps. Stop and redirect if offered; do not copy or retain them.
- P01–P05 are references, not a guarantee of anonymity. Remove names, employers, exact locations/dates, contact details and unique story combinations. Generalize or omit costs that could identify someone. No raw recordings or transcripts in Git, GitHub Issues or the public repository.
- Retain exact quotations only if accurately captured and permitted; otherwise use a labeled paraphrase. Never reconstruct a quotation from memory. A privacy scrub is required before any repository entry or assistant submission.
- Explain withdrawal honestly: private notes can be removed according to the agreed policy; publishing to Git history or distributing quotes makes complete recall difficult. Prefer owner-reviewed de-identified synthesis and avoid publishing identifying material in the first place.

Opening script, completed with the owner's actual research arrangements before use:

> “I'm learning about your current financial-management process, not assessing your finances or selling anything. We will take 15–20 minutes. Please do not share financial documents, identifiers or salary amounts. May I take brief de-identified notes for product research? [Explain storage, access, retention and withdrawal.] Recording is off; you may skip any question or stop. Any later quotation, repository sharing or AI-assisted analysis needs the explained permission. Is that okay?”

If permission is declined, do not take research notes or count undocumented answers as evidence. Record only a permitted process outcome. Do not promise security, compliance or deletion capabilities that FINNest has not implemented.

## Timebox and interview order

| Segment | 20-minute route | 15-minute route |
| --- | --- | --- |
| Purpose and consent | 0–2 min | 0–2 min |
| Q01–Q04: current behavior and recent problem | 2–6 min | 2–6 min |
| Q05–Q06: documents and last filing | 6–9 min | 6–8 min |
| Q07–Q08: alternatives and upload concerns | 9–12 min | 8–10 min |
| Q09–Q10: value and past payment | 12–14 min | 10–12 min |
| Concept and pricing, only after current problems | 14–18 min | 12–14 min |
| Prioritize one problem, clarify and close | 18–20 min | 14–15 min |

Use one useful follow-up per topic rather than reading every probe. Follow a concrete story when it matters; record skipped/not-asked questions instead of manufacturing answers. Ask permission to extend or arrange a follow-up if needed. Do not rush a participant into answering all ten questions.

## Core questions: ask before describing FINNest

| ID | Neutral question | Optional probe |
| --- | --- | --- |
| Q01 | How do you currently keep track of monthly income, expenses and savings, if at all? | Walk me through the last month you reviewed. What did you look at or do first? |
| Q02 | Tell me about the most recent financial-management problem that frustrated you, if one comes to mind. | Can you describe the last time that happened? What did you do to solve it? If none, what makes the current process work well? |
| Q03 | Roughly how many bank accounts or cards do you regularly use for everyday finances? | How do you bring their activity together, if you do? Counts or a broad description are enough; no identifiers or balances. |
| Q04 | Think of a month when savings differed from what you expected. What happened, and how did you work out why? | If savings decreased, was the cause clear? If this has never happened, record that. Do not suggest transfers or card repayments until after their account. |
| Q05 | How do you organize payslips, Form 16, AIS, investment documents or other tax records that apply to you? | Tell me about the last time you needed to find or share one. No document is needed for this interview. |
| Q06 | What was your most recent tax-filing or document-preparation process like? What, if anything, was difficult or time-consuming? | Who handled which steps? What was straightforward? If they have not filed, mark not applicable and ask only about document preparation. |
| Q07 | What finance apps, spreadsheets, bank tools or CA services have you used? What worked and what did not? | What made you start, keep using or stop using that approach? Product names are optional; no CA/person names. |
| Q08 | What, if anything, would concern you about uploading a bank statement to a financial application? | What information would you need before deciding? What would make you decline? Ask about AI/sharing/deletion only after spontaneous concerns and label prompted answers. |
| Q09 | If a tool could help with the problems you described, what specific job would make it useful to return to, if any? | What would you still prefer to do yourself or with your existing tools? What event would prompt a return? This is hypothetical, not observed retention. |
| Q10 | Have you ever paid for a financial-management or tax-preparation service? What made that worthwhile, or why have you not paid? | What service or outcome did you receive? Would you use it again? No receipt or exact amount is required. |

Across Q02/Q04/Q06, useful probes are: “How often does that happen?”, “What happened if you left it unsolved?”, and “What did it cost you in time or money, if you're comfortable describing that approximately?” Do not request income, balances or losses; use broad optional estimates only. Distinguish participant estimates from measured costs. Avoid agreeing that a problem is severe before the participant explains its impact.

## Concept and pricing: end of interview only

Record unaided problems and priorities before this section. If current behavior was not explored, skip the pitch and record the gap. Use the same brief description for comparability:

> “FINNest is a proposed tool for salaried individuals. You would upload supported CSV or selected bank/card PDF formats, review corrections and reconciliation warnings, see source-linked financial summaries, organize tax documents and optionally share selected material with your CA. It would not connect directly to your bank, file tax returns, calculate final tax liability or give investment recommendations. It is not ready for real financial documents, and specific supported providers are undecided.”

Ask: “What, if anything, fits a problem you actually described? What seems unnecessary or missing? What would make you prefer your current approach?” Then ask what upload/review effort would be acceptable, without soliciting an upload or claiming that stated willingness predicts behavior.

Present these **unvalidated options together**, with “neither/current method” equally available:

| Offer | Hypothesis to explain without overpromising |
| --- | --- |
| Free — ₹0 | Limited supported imports, corrections, basic dashboard and monthly summary; exact quotas unresolved |
| Plus — ₹999/year | More account/history capacity, recurring insights and an allowance for grounded financial questions; precise entitlements unresolved |
| One-time Tax Pack — ₹499 | Tax-document readiness/package support, not tax filing; proposed reporting-period unit and access window remain undecided |
| Neither / existing method | A valid choice; understand the reason without persuading |

Ask: “Which, if any, would you consider, and why? What would it replace? What would you need to see before deciding? Would seasonal use or repeat monthly use better fit you?” If relevant: “How would you expect a Tax Pack and annual plan to relate?” Record the description/version shown, price exposure, confusion and tradeoffs. Do not test arbitrary alternative prices or infer an optimum from five conversations.

The ₹1,999/year advanced-tax offer and CA subscription are later hypotheses, not V1 offers. If raised by a participant, explain that boundary and record the request without adding it to scope. Past payment for tax filing is evidence about that service, not proof someone will pay for a document organizer. No preorder, deposit, checkout or sales commitment is sought today.

## Close and prepare evidence

Ask the participant to choose the most important problem they actually mentioned and explain why. Reflect your understanding and invite correction. Ask separately whether they would welcome a follow-up; store contact consent privately, not in these files. Thank them regardless of product reaction.

After each interview, fill its [template](DAY_02_INTERVIEW_NOTES.md) only with permitted genuine notes, label prompted answers, uncertainty and unanswered questions, and run a privacy review. The user then supplies those de-identified responses for analysis. Do not turn blanks into “no problem,” a refusal into “would pay,” or hypothetical interest into validated demand.

## Completion gate and open arrangements

- Five distinct interviews actually completed and documented with appropriate permission; incomplete interviews are not silently counted.
- Findings tied to participant evidence; pain, alternatives, trust, pricing, dissent and Day 3 questions summarized and reviewed.
- Owner accepts DAY-002 research evidence and explicitly approves completion; repository PR/CI/review requirements also apply.
- No verified label or issue closure until those gates pass. No GitHub label change is authorized by merely saying it may be used if authorized.

Before interviewing, confirm recruiter/interviewer, participant availability, note storage/access/retention/withdrawal process and consent for de-identified repository/assistant use. Recruitment mix gaps can be recorded rather than filled with fictional participants. See [Day 2 open decisions](DECISIONS.md) and the [working evidence register](DAY_02_RESEARCH_SUMMARY.md). No interviews are performed by preparing these materials.

## Preparation validation (not research findings)

The following checks were run after preparing these materials:

| Check | Actual result | Limitation |
| --- | --- | --- |
| Manifest validation | PASS: 194 features, 85 working days | No manifest changes; does not validate customer demand |
| Existing tracker tests | PASS: 6 tests, 0 failures/errors | Executed outside sandbox for known Windows temporary-directory compatibility; no live issue mutation |
| Documentation checks | PASS: 100 local Markdown links resolve; fences/encoding checked | Does not certify external link availability or privacy compliance |
| Research-instrument coverage | PASS: 10 core questions, 5 blank templates, 50 unique evidence slots, 12 untested assumptions | Blank instruments do not count as interviews or findings |
| Whitespace | PASS: git diff --check for tracked changes and explicit whitespace inspection of the three new files | New untracked files are checked separately because git diff omits them |
| Scope preservation | PASS: master, source manifests, architecture, code and generated artifacts unchanged | No approval, verification, push or merge follows from these checks |

No application tests, financial fixtures, customer research or professional review results were invented. Final DAY-002 analysis remains pending genuine participant responses.

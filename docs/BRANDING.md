# FINNest — rename-ready branding

**Current working name:** `FINNest`. It has NOT been cleared as a registered mark. Similar-looking names are already active in financial services. Conduct professional trademark, domain, app-store and business-name checks before launch.

The single human-edited source for the visible brand is [`config/brand.json`](../config/brand.json):

```json
{"display_name":"FINNest","tagline":"Understand your money. Stay tax-ready."}
```

Only after explicit founder approval of a cleared replacement, use `python scripts/rebrand.py "New Name" --tagline "New tagline"` in a separately reviewed change. Commit/push require authorization. The GitHub sync workflow picks up the config and regenerates generated Markdown and the XLSX overview. Don't rename feature IDs (`FIN-001`, etc.), GitHub issue IDs, database primary keys or code route identifiers. They are stable process IDs, not a user-facing brand. Stable `tracking/*.xlsx` and `tracking/*.csv` filenames intentionally survive brand changes.

For eventual app launch, also review website domains, social handles, logo, intellectual property, legal entity name, email addresses, privacy/legal copy, mobile package identifiers, store listings and payment account names; these are not safely changed by a file search-and-replace.

## DAY-004 preliminary clearance — 2026-10-11

**Recommendation: keep FINNest internally configurable, but do not invest in public brand rollout until professional clearance or an approved replacement.** Material naming/confusion risk exists. This is a preliminary web check, not an Indian trademark search opinion, ownership determination or finding of infringement. Capitalizing FIN differently does not establish distinctiveness.

All exact URLs below were accessed on **2026-10-11**. Public websites/app listings confirm visible name use; company registration, trademark ownership and advertised professional credentials were not independently verified. No contact details or individual identities are reproduced.

| Check | Evidence | Finding / limit |
| --- | --- | --- |
| Indian financial businesses | [Finnest education finance](https://finnest.in/); [Finnest Funds Mart](https://www.finnestindia.com/) | Exact/similar financial-services branding on Indian websites; the latter advertises mutual-fund distribution. Material adjacency; no registry rights conclusion |
| Another Indian-facing platform | [FinNest financial partner directory](https://finnestco.com/) | Similar name/financial-partner positioning. Vendor user/partner counts and “verified” claims not substantiated by this review |
| International finance software | [Finnest Brazil](https://finnest.com.br/); [Brazil Apple listing](https://apps.apple.com/br/app/finnest/id6754052342); [Google Play listing](https://play.google.com/store/apps/details?hl=en_IN&id=br.com.finnest) | Exact finance-software name appears on official brand and app-store pages; a store URL does not prove availability in every country |
| Another personal-finance app | [Savings Tracker PH — Finnest](https://apps.apple.com/ph/app/savings-tracker-ph-finnest/id6737793710) | Similar personal-finance use creates search/app-store confusion risk; foreign rights not examined |
| Official Indian trademark search | [IP India public search](https://tmrsearch.ipindia.gov.in/tmrpublicsearch/) | Access page requires authentication/OTP and CAPTCHA. No authenticated wordmark/phonetic result set obtained; **Indian trademark clearance NOT completed** |
| Domains | Active sites above | `finnest.in`, `finnestindia.com`, `finnestco.com` and `finnest.com.br` visibly used. Availability/ownership of desired `.com`, `.app`, `.co.in` or alternatives **not verified**; no domain bought or reserved |
| Social handles / naming variants | App-store conflicts confirmed above; platform-by-platform handle checks pending | No exact handle availability claim. Counsel should search FINNEST, FIN NEST, FIN-NEST and phonetic/confusable spellings such as FINEST/FINVEST; this is a planned search list, not reported registry results |

Professional search should cover word and device marks, phonetic matches, status, owners, goods/services, priority and relevant jurisdictions. Initial class candidates are **9 (software), 42 (software services) and 36 (financial services)**; these are counsel-review hypotheses, not a filing classification decision. Review business names, passing-off risk, intended services and store searchability as well as registered marks. Do not conclude a name is safe because a domain is purchasable or one class has no exact match.

### Alternative working-name candidates

These are **unsearched creative candidates**, not available/clear names. None is selected or inserted into configuration; all need the same registry/domain/store/phonetic checks.

| Candidate | Reason to explore / tradeoff |
| --- | --- |
| LedgerLoom | Suggests assembling scattered records; could sound business-accounting oriented |
| RupeeTrace | Emphasizes source traceability and Indian context; may imply payments/tracking beyond scope |
| MonthSutra | Emphasizes understanding a monthly routine; test pronunciation and cultural interpretation |
| RecordMitra | Suggests help organizing records without promising financial advice; broader than finance |

Founder decisions: commission a professional FINNest search versus screen alternatives first; choose intended goods/services and launch jurisdictions; approve search budget/owner. Resolve before public naming expenditure. Repository remains **PersonalFinanceManager** and [brand configuration](../config/brand.json) remains unchanged. This review cannot verify FIN-005 or authorize rebranding.

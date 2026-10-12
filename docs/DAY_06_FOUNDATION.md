# DAY-006 — technical foundation and local staging

## Compact viewport PR regression — 2026-10-12

Review baseline: `codex/day-006-docker-security`, HEAD `441b6ef`, initially clean working tree. The founder reported job `114742308382` failing only the 320×568 overflow assertion. Read-only GitHub PR/job API requests timed out, so the remote PR identity, job revision and current CI status remain independently unverified. The local comparison against `master` contains the existing nine-file Docker remediation; this fix adds only CSS, browser coverage and this evidence section. No commit, push, issue change or Day 7 work is authorized here.

Reproduction used the unchanged production application, Node 22.23.3 and locked Playwright 1.64.0 Chromium in a disposable Debian Bookworm container. This matches the workflow's Node/build/browser tooling, but is not an Ubuntu runner clone. Initially its WenQuanYi system-font fallback passed. Installing `fonts-dejavu-core` selected DejaVu Sans and reproduced **exactly 30 passes / 1 failure, document width 344px at viewport 320px**. The source CSS hash matched the checkout. Thus the defect is reproducible with a supported system-font fallback; the remote runner's installed fonts could not be independently inspected.

At scroll position zero, measured rectangles and layout constraints were:

| Element / component | Before: x, y, width, right (px) | Computed sizing / cause | After: width / right (px) |
| --- | --- | --- | --- |
| `.h1 span`, [GlobeStory](../frontend/components/GlobeStory.tsx) | 22.39, 253.06, 321.39, 343.78 | Inline width `auto`, min-width `0`; 42px font and `white-space: nowrap` exceed the heading's 258.70px content width | 244.88 / 267.27 |
| `.hero-cta .primary`, GlobeStory | 22.39, 458.05, 314.30, 336.69 | Width 314.30px, min-width `auto`, nowrap text plus 42px horizontal padding in a 275.22px flex parent | 275.22 / 297.61 |
| `.sample-label`, [SampleDashboard](../frontend/components/SampleDashboard.tsx) | 16, 4218.08, 307.55, 323.55 | Width 307.55px, min-width `0`, nowrap monospace badge in 288px `.demo-top` | 288 / 304 |
| `.final-inner`, [ProductStory](../frontend/components/ProductStory.tsx) | 19.19, 9938.83, 302.61, 321.80 | Min-width `auto`; 61px heading imposes a 302.61px grid minimum on `#finale`, whose available content width is 281.60px | 281.63 / 300.81 |

The decorative `.globe-atmosphere` also extends beyond the viewport, but its existing clipped `.stage` contains it; it does not cause document overflow and was left intact. Eleven sampled scroll positions (hero, all chapters, money flows, demo, how, trust, finale and footer) expose the same document-wide defect.

The [CSS fix](../frontend/app/globals.css) is restricted to the existing compact breakpoint, ≤370px: responsive hero/finale heading sizes and parent-constrained, wrapping CTA/badge text. A focused hit-target test then caught the reflowed secondary link intercepting the pause control; allowing the hero description its full parent width and reducing the CTA gap to 10px resolves that regression. There is no new global clipping or width rule. Layouts at 390px and above retain their existing CSS. The [browser harness](../frontend/tests/check-app.mjs) retains the strict overflow assertion at all four sizes, now waiting for fonts, checking globe control bounds and center hit targets, measuring all eleven page positions, saving full-page screenshots and closing each context even on failure.

Verification after the fix (synthetic data only):

- `npm run build`: PASS in Linux Node 22, production `/` and `/_not-found` routes generated.
- `npm run lint`, `npm run typecheck`, `npm test`: PASS; **5/5** exact financial fixture tests, including paise and reversible corrections.
- `npm run test:browser`: **31/31 PASS** with DejaVu Sans; scrollWidth equals viewport width at **320, 390, 768 and 1440px**, across eleven positions each. Globe rotation/drag/zoom/reset, anchoring, mocked location, transaction correction, mobile touch/menu, keyboard outline and initial/runtime reduced motion pass. The original pre-fix suite reproduced **30/31**, with the single reported overflow failure.
- Focused 320px inspection also exercised the menu, Escape, primary CTA and focus outline. Additional Playwright measurements confirm all four 44px globe controls are reachable and the hovered marker tooltip fits inside each of the four required viewports. Before/after hero, finale, dashboard and full-page screenshots are local ignored test evidence, not customer records. Compact vertical story/location-panel crowding predates this fix and is not represented as resolved by the horizontal-overflow check.
- `python scripts/validate_manifest.py`: PASS, 194 features / 85 days. `python scripts/check_docs.py`: local Markdown targets pass; external URLs and fragments are not validated.
- `python -m unittest discover -s tests -v`: **6/6 PASS** with ordinary filesystem permissions; the first sandbox run had one temporary-directory permission error, not a tracker assertion failure.
- `git diff --check`: PASS. Review and a new remote CI run remain required before merge; local tests do not establish remote CI success or security approval.

**2026-10-12 · implementation for founder review; not verified or released.**

**Current remediation status:** the original scaffold was committed as `908693a` and integrated into baseline `bc307f55fd8703dda78d1f085fdb55508e26a80f`. The Docker remediation below is on `codex/day-006-docker-security`, awaiting founder acceptance and commit approval. Earlier test results, Git state and issue-lookup statements in this report are historical snapshots, not current acceptance. No Day 7 implementation is included.

## Exact scheduled task and dependencies

The authoritative [daily manifest](../data/daily_plan.json) records:

- ID: **DAY-006**, week 2, phase **Architecture and secure foundations**.
- Task: **Scaffold Next.js, FastAPI, PostgreSQL, CI and local staging**.
- Acceptance: **Reviewed work artifact or documented validation evidence**.
- Owner: **Unassigned**.

There is no separate title/description field or explicit dependency list in this row. The task text above is used unchanged. Practical dependencies are the approved Day 5 design/fictional fixtures, configurable branding, Node/npm, Python, Docker for PostgreSQL/staging and access to dependency registries. No new feature or day IDs are created.

Related features: FIN-005 (brand configuration), FIN-006 (landing page/waitlist), FIN-127 (modular monolith and migrations), FIN-128 (CI checks), FIN-129 (environment separation). This foundation contributes to those features; it does not satisfy the waitlist, migrations, branch-protection or production-separation acceptance in full. Their existing target days/releases remain unchanged, including the later FIN-127–129 target: early scaffold work is an incremental dependency, not feature completion. DAY-007 remains **Design canonical ledger, ownership, Decimal amounts and migrations**; DAY-008 owns authentication.

## Before and after audit

At start, `master` had HEAD `7ef5083` and committed Day 5 work (`e55512d`). Two pre-existing untracked files were present: root `package-lock.json` (empty root package graph) and `docs/design/day05/reference/package.json` (`dev: py -m http.server 8000`). Both are preserved. The latter is a Python static-server shortcut, not React/Next.js. `tools/tracker/package.json` is the existing Excel renderer, not a website build.

Before this task: executable standalone V4 HTML/CSS/JavaScript and design contracts; no frontend scaffold, React components, backend or application CI. Existing CI tested manifests/tracker. Day 5's archived browser report had two failures: reduced-motion decoration and compact transaction clipping.

Now: a dedicated [frontend package](../frontend/package.json), FastAPI application, PostgreSQL Compose service, application CI and browser/financial/backend tests. The archived V4 files and historical evidence are unchanged. There is no root forwarding script: use `npm --prefix frontend run dev` if convenient, leaving the founder's shortcut unambiguous. A separate frontend package is the planned modular-monolith browser client, not a second competing app.

## Implemented boundaries

| Area | Implementation | Deliberately not implemented |
| --- | --- | --- |
| Next.js App Router / TypeScript | Server page/layout load `config/brand.json`; static product copy plus interactive React islands | User accounts, live uploads, billing, tax engine, CA grants |
| V4 visual experience | Original CSS composition/geography, navigation, canvas globe/story, category paths, fictional workspace, trust/footer sections | Generic template replacement, 3D/map dependency, bank-network claims |
| Canvas adapter | Separate `lib/globe-runtime.js`, scoped native listeners/AbortController, RAF/observer cleanup, bounded DPR, batched scroll measurements, stable stage, rounded location with stale-callback guard | Renderer is still JavaScript with a JSDoc boundary; strict TypeScript does not type-check its internal geometry/state. Fully typed renderer and broader device/performance profiling remain follow-up work |
| Finance | Decimal-based selectors over nine immutable synthetic rows; correction overlays, exact paise, chart proportions from fixture amounts, partial-coverage notice and Sample Data badge | Canonical production ledger schema, tax treatment or true-savings calculation |
| Location | Explicit click, immediate integer-degree rounding before retained state, clear including pending requests, no app network/persistence, denial/error handling | IP lookup, reverse geocoding, analytics, backend location storage; normal browser/OS permission services are outside app control |
| FastAPI | `/health/live`; `/health/ready` checks PostgreSQL with bounded connection/query timeouts and sanitized failure | Financial endpoints, CORS grants, automatic schema creation, auth bypass routes or public API docs |
| PostgreSQL / staging | Synthetic named volume; no host DB port; API/frontend loopback ports; non-root API/frontend processes | Production database, TLS/secrets manager, backups, real-data permissions or public deployment |
| CI | Separate read-only application workflow: lint/type/unit/build/browser, backend tests/real database probe, local-doc links, Compose config | Changes to tracker workflow, automatic issue verification, deployment or branch protection |

Retained interactions include auto-rotation, drag/touch pointer handling, markers, zoom/pause/reset, all four chapters and fade, optional area focus/clear, flow selection and reversible credit correction. Integration corrects the two known Day 5 failures, uses incremental vertical drag and shortest-arc location focus, improves menu Escape/labels, hides inactive chapter controls from keyboard interaction, and replaces the contradictory “No personal data collected” footer.

Reset resets globe orientation/zoom; **Clear** removes location. Integer-degree rounding is not guaranteed anonymity. No genuine location was used in tests. Canvas marker information has a text/button equivalent in Money flows. No accessibility certification is claimed.

## Developer workflow

Prerequisites: Node 22.13+ (Node 22 LTS used by CI/container), npm, Python 3.13, and Docker Desktop/Compose for the full stack. The host verification used Node 25.2.1; Linux container validation covers the intended Node 22 runtime. Versions are locked in the frontend lockfile and backend requirements. Consult the [official Next.js installation guide](https://nextjs.org/docs/app/getting-started/installation) and [FastAPI container guide](https://fastapi.tiangolo.com/deployment/docker/) (accessed 2026-10-12); this is an internal scaffold, not a production deployment recipe.

Frontend, from repository root:

```powershell
cd frontend
npm ci
npm run dev
```

Open `http://127.0.0.1:3000`. Stop with Ctrl+C. The frontend works independently of the API because all money data is synthetic and local. In another terminal from `frontend/`:

```powershell
npm run lint
npm run typecheck
npm test
npm run build
npm run start
```

Stop the dev server before starting the production preview on the same port. Stop either server before `npm ci` on Windows: loaded native modules can prevent npm from replacing files. For browser regressions, leave the production preview running, then use another `frontend/` terminal:

```powershell
# With an already installed Chrome, no browser download needed:
$env:DESIGN_BROWSER_CHANNEL = 'chrome'
npm run test:browser
# Alternatively install Playwright Chromium once, omit that environment override,
# and run the same script. CI installs Chromium explicitly.
```

Browser results/screenshots go to ignored `frontend/test-results/`. Tests always mock location. `APP_URL` can point to another loopback port, with a trailing slash. Do not point tests at a site with actual customer data.

Backend without containers, from repository root:

```powershell
python -m venv backend/.venv
backend/.venv/Scripts/python.exe -m pip install -r backend/requirements.txt
cd backend
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001 --no-access-log
```

Use `.venv/bin/python` on Unix. `/health/live` works without DB configuration; `/health/ready` intentionally returns 503 unless an available synthetic PostgreSQL `DATABASE_URL` is supplied. Do not print connection strings or paste production values. Stop with Ctrl+C.

Full local staging from repository root:

1. Start Docker Desktop. Copy [.env.example](../.env.example) to ignored `.env` **only if it does not exist**; set a disposable URL-safe local password. Never overwrite existing settings. This task created a fresh ignored local password without printing it.
2. Stop standalone servers on ports 3000/8001 to avoid port conflicts.
3. Run `docker compose up --build -d`.
4. Visit `http://127.0.0.1:3000`, `http://127.0.0.1:8001/health/live` and `/health/ready`. `docker compose ps` reports health. Do not expose these ports beyond loopback.
5. Stop using `docker compose down`. This preserves the synthetic database volume. Do not delete volumes without an intentional data-reset decision.

The local PostgreSQL role is the disposable initializer/owner; it is not the production least-privilege role model. DAY-007 must design runtime/migration permissions. Images and development tooling need further production hardening; no deployment is authorized.

Original prototype remains available:

```powershell
cd docs/design/day05/reference
npm run dev -- --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/FINNest_Interactive_Globe_V4.html`; stop with Ctrl+C. This npm command still invokes Python, and the archived source retains its documented Day 5 defects. It is separate from the real Next.js route.

## Historical scaffold validation and remaining issues

| Check | Actual result on 2026-10-12 |
| --- | --- |
| Frontend lint / route type generation / TypeScript | PASS on Windows and in the final Node 22 Linux image |
| Frontend unit tests | **5/5 passed** on Windows and Linux: three golden classifications, immutable/undo behavior, exact paise/large values/chart proportions |
| Next.js production build | PASS on Windows and Linux; `/` prerendered successfully |
| Browser regression suite | **31/31 passed**, installed headless Chrome against the real production route; [machine-readable evidence](evidence/day06/app-checks.json) |
| Development startup / lifecycle | `npm run dev -- --port 3001` served HTTP 200; observed one active globe RAF and one canceled RAF after Strict Mode remount, correct ₹85,600 reclassification and no page errors. A bounded check, not proof of every lifecycle race |
| Backend tests | **5/5 passed**; Starlette/httpx deprecation warning remains |
| PostgreSQL / API | Container DB/API healthy; actual SQL `SELECT 1` succeeded; `/health/live` and `/health/ready` both returned HTTP 200 with expected sanitized JSON |
| Local image builds | Both API and frontend built successfully; frontend lockfile validated by clean Linux `npm ci`. Final lockfile also accepted by Windows `npm ci --dry-run` |
| Manifest / IDs / releases | PASS: 194 unique FIN IDs, 85 unique daily IDs; V1 140, V1.5 14, V2 20, V3+ 8, Future 12; source manifests unchanged |
| Existing tracker tests | **6/6 passed**; run with temporary-directory access outside the Windows sandbox |
| Tracker npm build | PASS in isolated ignored `tmp/day06-tracker-check`, using existing ExcelJS; 194 feature/85 daily rows. Actual tracked workbook untouched |
| Original website shortcut / source hashes | PASS: founder's unchanged npm/Python command served byte-identical HTML, HTTP 200; all nine approved reference hashes match |
| Documentation / whitespace | Local Markdown file-target checker and Git whitespace checks pass; remote links/heading fragments excluded. New authored files also inspected separately because normal Git diff omits untracked files |
| Remote GitHub CI and issue acceptance | **Not verified**: nothing pushed, both GraphQL and bounded REST issue lookups timed out |

Screenshots from the migrated route: [desktop](evidence/day06/desktop-hero.png), [mobile](evidence/day06/mobile-hero.png). Desktop/mobile heroes and compact transaction layout were visually inspected; real devices, screen readers, full contrast measurement and performance profiling remain pending. The React skill review covered component boundaries, client-only effects/cleanup, immutable financial state, SSR-safe initialization and semantic controls. No certification is implied.

Earlier failures were retained as diagnostic history, then addressed: sandbox process/temp-file restrictions; two JSX conversion errors; backend test import path; CommonJS harness lint failure; a Windows native-module lock during `npm ci` while the server was running; missing status.json in the isolated tracker fixture; Docker Hub TLS timeouts; a Windows-generated lockfile missing optional Linux entries; and the runtime motion control state mismatch. Direct image pulls, corrected Linux lock resolution and the final reruns resolved those execution/build defects. Local HTTP probes bypassed the environment proxy after a proxy-generated 504; the API itself returned 200. Next.js dev initially generated a new frontend AGENTS.md; automatic agent rules were disabled and only that newly generated file removed, preserving the authored root instructions.

These are local results, distinct from GitHub CI, which cannot run until changes are reviewed and published. No generated tracker output in the actual repository was regenerated.

Dependency review: `npm audit --omit=dev` reported **0 vulnerabilities** at this snapshot. The full audit reported **5 high-severity entries in the lint dependency chain** (`eslint-config-next` → Next lint plugin → fast-glob/micromatch/braces; GHSA-vfj7-8cjw-p6xm). These are not five independently proven application vulnerabilities. No patched compatible resolution was offered without downgrading Next lint tooling to an older major; no forced downgrade/override was applied. ESLint 10 was tested but had incompatible plugin peer ranges, so the lock retains compatible ESLint 9.39.5 with its deprecation warning. Track a compatible toolchain update before public release; do not feed untrusted patterns to developer tooling or claim a clean full audit. Python tests also emit a Starlette/httpx deprecation warning; migration to its successor test transport is follow-up, not a failing health check.

Outstanding: public asset/brand clearance, actual-device touch/voiceover/contrast review, complete renderer typing and paused/offscreen rendering optimization, qualified security/privacy reviews, and all previous real-data gates. No new customer research, professional approval or tax correctness is implied.

## GitHub acceptance and Day 7 handoff

The read-only `gh issue list --repo Tejanshu22/PersonalFinanceManager --state all --search 'DAY-006 in:title'` lookup failed first with sandbox proxy refusal and then with a TLS handshake timeout outside the sandbox. **Existence/number/current state are unconfirmed**, not “missing.” Do not create a duplicate on that basis. No issue was created, closed or labeled.

If a successful later lookup proves it absent, proposed issue title: **[DAY-006] Scaffold Next.js, FastAPI, PostgreSQL, CI and local staging**. Preserve manifest acceptance (“Reviewed work artifact or documented validation evidence”) and attach this operational checklist as evidence:

- Clean checkout dependency installation and Next.js start/build are reproducible; configurable V4 UI and all synthetic interactions retained.
- Exact financial cases, location mocks, regression checks, backend health/readiness and real PostgreSQL connection evidence reviewed.
- CI covers the scaffold while existing tracker/tests/generated ownership remain intact.
- Local startup/shutdown, synthetic-only boundaries and unresolved findings documented; no source-ID/release changes.
- Human accepts the scoped Day 6 artifact, relevant checks pass on the reviewed commit, and the AGENTS.md merged-PR/CI/review gate is met before explicit verified/closure approval.

DAY-007 should use the monolith/database foundation to design the canonical ledger, ownership, exact amount/date/currency conventions and reversible migrations with independent fixtures. Do not treat this sample UI fixture as the production schema. Authentication remains Day 8. No remapping of the 85-day schedule is needed; earlier Day 1 dependency proposals remain separately pending. FIN-006's waitlist remains open work. Nothing here authorizes commits, pushes, real-data onboarding or public release.

## Historical scaffold changed-file inventory

Modified: `.gitignore`, `README.md`, `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/RELEASE_CHECKLIST.md`, `docs/SCREENS.md`, `docs/SECURITY.md`. The tracked diff is 33 additions and 4 removals; the 37 new task files below are not included in ordinary Git diff statistics.

```text
.dockerignore
.env.example
.github/workflows/application.yml
backend/Dockerfile
backend/app/__init__.py
backend/app/main.py
backend/pytest.ini
backend/requirements.in
backend/requirements.txt
backend/tests/test_health.py
compose.yaml
docs/DAY_06_FOUNDATION.md
docs/evidence/day06/app-checks.json
docs/evidence/day06/desktop-hero.png
docs/evidence/day06/mobile-hero.png
frontend/Dockerfile
frontend/app/globals.css
frontend/app/layout.tsx
frontend/app/page.tsx
frontend/components/GlobeStory.tsx
frontend/components/MoneyFlows.tsx
frontend/components/Navigation.tsx
frontend/components/ProductStory.tsx
frontend/components/SampleDashboard.tsx
frontend/eslint.config.mjs
frontend/lib/flow.ts
frontend/lib/globe-runtime.js
frontend/lib/land-points.json
frontend/lib/sample-finance.ts
frontend/next-env.d.ts
frontend/next.config.ts
frontend/package-lock.json
frontend/package.json
frontend/tests/check-app.mjs
frontend/tests/sample-finance.test.ts
frontend/tsconfig.json
scripts/check_docs.py
```

Pre-existing untracked files retained separately: root `package-lock.json` and `docs/design/day05/reference/package.json`. Ignored dependencies, build outputs, local-only `.env`, virtual environment and temporary verification copies are not deliverables. Nothing is staged, committed or pushed.

Final local staging is running for review at `http://127.0.0.1:3000` with API on port 8001. Stop it with `docker compose down` before using the default native development ports. The temporary native dev/production/prototype test servers were stopped.

## DAY-006 Docker security remediation — 2026-10-12

### Baseline, causes and changes

The remediation began on clean `master` at `bc307f5`. The founder authorized fixing both review findings before Day 7. Root `package-lock.json` and `docs/design/day05/reference/package.json`, previously untracked, were included in `908693a`; both remain unchanged here. The root lock contains an empty package graph (redundant for the frontend); the prototype package contains only the Python-server shortcut. Neither contains credentials. No tracked environment settings, node_modules, build output or real financial records were identified; the reviewed `.env.example` contains a disposable placeholder only.

Both Compose services build with repository-root context. There are no frontend/backend Dockerfile-specific ignore files. Original `.env`/`.env.*` Docker rules applied only at root, while `COPY frontend ./` could copy nested environment settings. Separately, the final frontend stage copied the complete build workspace, shipping development dependencies even though `npm audit --omit=dev` was clear.

- [.dockerignore](../.dockerignore) now excludes environment files at every depth (`**/.env`, `**/.env.*`), nested Git metadata, private-key filename patterns and TypeScript build caches. The safe root example stays in Git but is deliberately excluded from images too; no broad example exception is needed.
- [Frontend Dockerfile](../frontend/Dockerfile) separates dependency installation, build and runtime. Before source COPY, a read-only BuildKit mount checks the actual filtered context and fails if any `.env*` entry remains or inspection fails. Values are never printed. This also detects Dockerfile-specific exclusion regressions during a real build.
- [Next configuration](../frontend/next.config.ts) enables standalone output only when Docker sets `BUILD_STANDALONE=1`. Tracing covers the repository root for existing outside-package imports. Ordinary native build/start remains supported. See [official standalone output documentation](https://nextjs.org/docs/app/api-reference/config/next-config-js/output), accessed 2026-10-12.
- Runtime copies only traced standalone output, `.next/static` and `public` (currently empty), then starts `node frontend/server.js` as UID/GID 1000 (`node`). Port 3000 and hostname are explicit. All existing security headers remain present. Compose is unchanged: frontend/API publish to 127.0.0.1 only; PostgreSQL has no published host port.
- [Container regression check](../scripts/check_container_security.py) creates fake environment sentinels, forces the real context guard, builds the actual Compose images and scans every saved build/runtime/backend image layer. It checks values as well as filenames, so deleting a copied sentinel in a later layer cannot produce a false pass. It refuses unreviewed Dockerfile-specific ignore overrides, preserves existing files, and removes only its own sentinels/directories in `finally`.
- [Application CI](../.github/workflows/application.yml) gains the same container check and local health probes. Job timeouts bound execution; existing read-only permissions and master/PR triggers are preserved. Tracker CI is unchanged. This workflow change has local validation only; its remote execution is not independently verified.

### New verification evidence

The [container evidence](evidence/day06/docker-security.json) and [browser evidence](evidence/day06/docker-browser-checks.json) record this remediation separately from the historical scaffold report. Browser tests use synthetic finances and mocked location only. No genuine location or financial documents were collected.

| Command / inspection | Observed result |
| --- | --- |
| `python scripts/check_container_security.py` | PASS: 24 synthetic files across root, frontend, backend and nested folders; existing root `.env` preserved byte-for-byte; all sentinels removed |
| Harness: `docker build --no-cache-filter build --target build -f frontend/Dockerfile -t personal-finance-local-frontend-security-build .` | PASS: actual filtered context guard ran before COPY; builder layer inspection found no environment paths or sentinel bytes |
| Harness: `docker compose build frontend api` | Both images built; runtime and API layer inspection found no environment paths or sentinel bytes |
| `docker compose config --quiet`; `docker compose up -d --no-build --wait --wait-timeout 90` | PASS; existing synthetic DB volume retained, no reset |
| HTTP probes using Python urllib with local proxy bypass | Frontend `/` 200, expected brand/globe/Sample Data and headers; API live/ready both 200 with expected sanitized JSON |
| `docker compose exec -T db pg_isready -U local_app -d finance_synthetic`; `psql -U local_app -d finance_synthetic -tAc 'SELECT 1'` | Accepting connections; result `1` |
| From frontend: `npm run lint`; `npm run typecheck`; `npm test`; `npm run build` | PASS; five exact financial tests; native production build passes with default output after sentinel cleanup |
| `DESIGN_BROWSER_CHANNEL=chrome npm --prefix frontend run test:browser` (PowerShell environment assignment locally) | 31/31 PASS against the remediated Docker route: globe/scroll/control/location/reduced-motion/category/correction/mobile/keyboard checks; no page errors or third-party requests |
| `backend/.venv/Scripts/python.exe -m pytest -q backend` | 5/5 PASS; existing Starlette/httpx deprecation warning remains |
| `python -m unittest discover -s tests -v` | 6/6 tracker tests PASS |
| `python scripts/validate_manifest.py` | PASS: 194 features / 85 days; manifests and release assignments unchanged |
| `python scripts/check_docs.py`; `git diff --check` | PASS; local file links only, not external URLs or heading fragments |

The native frontend build was initially run while fake sentinels existed and correctly reported loading local environment files outside Docker. It was repeated successfully after cleanup. Docker builds never loaded those files. Git emits the existing LF-to-CRLF informational warnings; no whitespace failures occurred. No build, unit or browser failures remain in the remediation run.

The pre-remediation local image measured **1,193,226,713 bytes**. The standalone image is **420,660,300 bytes**, a **64.7% reduction** (Docker's local image Size metric, not registry transfer size; exact current bytes are in the evidence). Application contents are `/app/frontend/server.js`, `.next` server/static artifacts, traced runtime `node_modules`, package metadata and `public`. Raw application source, raw financial fixture JSON, tests, repository history, environment files and the listed development packages are absent. The standard Node/Debian base still includes its normal OS and bundled package-manager components; this is not a distroless image, OS vulnerability scan or security certification.

### Current dependency disposition

On Windows Node 25.2.1 / npm 11.6.2 against `https://registry.npmjs.org/`, actual `npm audit --omit=dev --json` reports **0 vulnerabilities**; full `npm audit --json` still reports **5 high entries**. `npm explain braces` confirms this single chain:

`eslint-config-next@16.4.0` (direct dev) → `@next/eslint-plugin-next@16.4.0` → `fast-glob@3.3.1` → `micromatch@4.0.8` → `braces@3.0.3` (transitive dev).

The underlying [GHSA-vfj7-8cjw-p6xm / CVE-2026-93687 advisory](https://github.com/advisories/GHSA-vfj7-8cjw-p6xm), accessed 2026-10-12, covers stack-exhaustion denial of service from deeply nested brace patterns and lists no patched version. Registry checks `npm view braces version` and `npm view eslint-config-next version` returned 3.0.3 and 16.4.0. npm's suggested 14.2.35 lint-config downgrade changes major versions and is not a compatible fix for this Next 16 scaffold. No forced fix, override, dependency upgrade or lockfile change was applied.

All five affected packages, plus ESLint, TypeScript, tsx, Playwright and Prettier, are absent from the runtime layers. They remain in the development/build environment. No application HTTP input is passed into lint globs, but developer/CI availability risk remains when processing malicious patterns/configuration. Mitigations are runtime separation, version-controlled tooling, read-only CI without production credentials and bounded jobs; these do not patch the underlying vulnerability. Proposed owner: technical lead, with founder review of this residual risk and compatible-update rechecks before public release. The zero production audit describes the npm production graph only, not every binary or OS package in the image.

### Acceptance and Day 7 boundary

Both Docker review findings now have local remediation evidence. Founder review, explicit commit/push approval, relevant remote CI on the reviewed commit and the repository acceptance gate remain required. Current remote GitHub CI/issue state has not been independently confirmed; historical failed lookups are not evidence of absence or current failure. No issue, label, commit or push was changed by this remediation.

Day 7 can resume from the accepted, committed/integrated remediation baseline after those approvals. O-04 monetary conventions remain pending and must not be inferred from this Docker work. Real-data onboarding, auth, ledger/migrations, bank uploads, tax calculations, payments and CA sharing remain outside this change.

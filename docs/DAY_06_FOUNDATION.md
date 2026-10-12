# DAY-006 — technical foundation and local staging

**2026-10-12 · implementation for founder review; not verified or released.**

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

## Validation and remaining issues

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

## Changed-file inventory

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

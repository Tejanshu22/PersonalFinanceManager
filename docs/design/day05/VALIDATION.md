# DAY-005 validation and integration backlog

**Run date: 2026-10-12. Target: unmodified founder V4 prototype, not a production frontend.** Creative approval does not imply technical acceptance. Supplied `reference/TEST_RESULTS_V4.json` is historical upstream evidence, distinct from this run.

## Independent browser results

Installed Chrome, headless, driven by the existing bundled Playwright package; no dependency installation. The first launch attempt found no bundled Chromium executable; the next installed-Chrome attempt hit sandbox EPERM. The allowed execution outside that sandbox succeeded. Tests use an isolated context, a loopback server and synthetic geolocation callbacks installed before page code. No genuine location or personal financial data was used.

**28 checks: 26 passed, 2 failed; harness exit code 1.** Exact outcomes: [JSON report](evidence/reference-checks.json). Reproduction: [README](README.md). These results neither certify accessibility/security nor prove real-device/browser coverage.

| Area | Actual result / limitation |
| --- | --- |
| Desktop globe | Auto-rotation, pause, marker hover, dragging, zoom/reset passed through observed canvas geometry/tooltip state |
| Scroll | Four indicators observed at scroll positions 0/750/1450/2200; canvas y stayed 0; exit opacity 0.30303 at 2750. Forward/backward scrolling did not rotate paused markers. Broader viewport/device center stability remains a manual/integration test |
| Location | No initial request; mocked grant rounded 25.4358/81.8463 to displayed 25°N/82°E; clear removed marker; deny/timeout/unavailable/missing API/insecure cases passed. Source inspection finds rounded-only retained pair; black-box tests do not directly inspect closure memory or OS permission UX |
| Financial interaction | Five route choices and three correction states/undo matched declared reference totals. This tests toggled sample numbers, not a real ledger engine |
| Responsive / input | Document-width checks passed at 1440×900, 768×1024, 390×844 and 320×568. Mobile menu/CTA/location control and synthetic touch drag passed; keyboard focus indicator and arrow movement passed |
| Narrow transaction layout | **FAIL:** at 320×568 each tested row measured 212px wide but content scrollWidth was 299px. Hidden page overflow masks clipped monetary columns; document-width checks alone are insufficient |
| Reduced motion | Initial automatic globe rotation stopped, but **FAIL:** canvas pixels continued changing from decorative animation. Full reduced-motion requirement is unmet |
| Runtime/network | No page errors or third-party requests observed during these local scenarios. This is bounded observation, not a security audit |

Screenshots from this run: [desktop hero](evidence/desktop-hero.png), [desktop dashboard](evidence/desktop-dashboard.png), [desktop mocked location](evidence/desktop-location-mock.png), [mobile hero](evidence/mobile-hero.png), [mobile mocked location](evidence/mobile-location-mock.png), [compact dashboard showing clipping](evidence/compact-mobile-dashboard.png). Hero, mobile-location and compact-dashboard images were visually inspected. Element screenshots spanning multiple viewports may include a fixed header within the captured element; do not interpret that capture artifact as ordinary full-page layout.

## Required refinements when integrated into components

These are **unfixed in the archived source**. Preserve the approved composition, not the defects. See [component contracts](INTEGRATION.md).

| Ref | Finding / evidence | Required follow-through |
| --- | --- | --- |
| V4-R01 | Browser failure: decorative movement under reduced motion | Freeze all time-based decoration; dynamic preference changes update labels/state consistently |
| V4-R02 | Browser failure: narrow transaction row clipping | Stack transaction labels/category/amount at small widths; verify all values visible at 320px and 200% zoom |
| V4-R03 | Source inspection: location focus/reset assign orientation immediately; vertical drag uses displacement from initial y | Use shortest-arc easing when motion allowed, immediate placement when reduced; incremental drag delta; single pointer ownership |
| V4-R04 | Source inspection: standalone IIFE has global listeners and continual RAF; no component disposal | Client-only effect, single render owner, offscreen suspension, cleanup, stale-callback guard, Strict Mode test; no window/navigator during SSR |
| V4-R05 | Source inspection: footer says no personal data collected despite optional location; pending/hover cleanup incomplete | Accurate memory-only purpose disclosure; clear during pending request; ignore late completion; remove location tooltips; no telemetry |
| V4-R06 | Source inspection: hardcoded financial toggles/bar heights; malformed closing strong tag for uncertain subtext | Derive totals/charts from exact fictional rows and correction overlay; update uncertainty explanation and announce changes |
| V4-R07 | Source inspection: hardcoded reference brand; menu label does not follow expanded state | Inject central brand config in consuming shell; proper menu labels/Escape; keyboard-accessible marker equivalents; screen-reader/contrast review |
| V4-R08 | Reference has no waitlist, upload, authentication, payments, tax engine or CA grant | Keep planned functionality labeled; FIN-006 remains unsatisfied; do not implement those flows as a design side effect |
| V4-R09 | Coarse geographic points supplied inside HTML; public asset provenance not verified | Confirm source/license suitability before public release; do not claim bank-network or authoritative cartography |

## Repository checks

| Check | Actual result |
| --- | --- |
| `python scripts/validate_manifest.py` | PASS: 194 features, 85 working days |
| `python -X utf8 -m unittest discover -s tests -v` | Initial sandbox run: 5 passed, 1 temporary-directory PermissionError (WinError 5). Allowed rerun outside sandbox: **6/6 passed**, 0.045 seconds; no tracker code changed |
| Local documentation targets (ad hoc Python scan of tracked and new Markdown outside fenced code) | PASS: 214 file targets across 34 documents, 0 missing; remote URLs and heading fragments not tested |
| Feature/day uniqueness and release counts | PASS: 194 unique features, 85 unique days; V1 140, V1.5 14, V2 20, V3+ 8, Future 12 |
| Original-reference byte/hash comparison | PASS: all 9 copies match source bytes, lengths and SHA-256 manifest |
| Synthetic fixture calculation with Python Decimal | PASS: 3 correction cases × 7 exact totals; 9 source rows unchanged. Specification check, not a built financial engine |
| JavaScript harness syntax | PASS: `node --check docs/design/day05/check-reference.cjs` |
| `git diff --check` and new authored-text whitespace scan | PASS; 7 new authored text files checked separately because untracked files are not covered by normal Git diff. Byte-preserved source archive excluded from authored-whitespace normalization |
| Protected files / Git review | No diff to source manifests, brand configuration or generated Markdown. Tracked diff: 3 files, 24 added lines; 22 additional untracked design/evidence files. No staged files or branch change |

Application lint/type tests and a production build are **not available** because there is no application scaffold; the tracker workbook build is not a substitute. No live financial fixture suite exists. Checks above validate the reference and specification only. No issue/bootstrap/progress-generation command ran.

## Changed-file inventory

Modified: `README.md`, `docs/SCREENS.md`, `docs/DECISIONS.md` (24 added lines, no removals). All 22 new files are below, relative to `docs/design/day05/`:

```text
README.md
INTEGRATION.md
VALIDATION.md
sample-finance.json
reference-manifest.json
check-reference.cjs
reference/ASTRA_DAY5_V4_INTEGRATION_PROMPT.md
reference/FINNest_Interactive_Globe_V4.html
reference/README.md
reference/TEST_RESULTS_V4.json
reference/FINNest_V4_Dashboard.png
reference/FINNest_V4_Desktop_Hero.png
reference/FINNest_V4_Location_Desktop.png
reference/FINNest_V4_Mobile_Hero.png
reference/FINNest_V4_Mobile_Location.png
evidence/reference-checks.json
evidence/desktop-hero.png
evidence/desktop-dashboard.png
evidence/desktop-location-mock.png
evidence/mobile-hero.png
evidence/mobile-location-mock.png
evidence/compact-mobile-dashboard.png
```

## Manual and future component verification steps

- Preview locally using the README; check desktop hero, four chapters, exit and return. Check globe center at each chapter rather than only fixed canvas bounds. Rotate while scrolling; ensure scroll never changes yaw direction. Verify controls do not intercept later sections.
- On actual iOS/Android, test horizontal drag and normal vertical page scrolling, pointer cancel, toolbar resizing and orientation changes. Current touch evidence is synthetic Chrome input only.
- Use keyboard alone through navigation, chapter CTAs, globe, flows and correction. Check no invisible focus stops; test menu Escape/focus restoration and screen reader announcements. Measure contrast on actual rendered backgrounds and verify 200% zoom/short-height layouts.
- Test every mocked location outcome, invalid coordinates, rapid request/clear, late callbacks, unmount and tooltip clear. Never test with genuine user location. Inspect storage/network and all telemetry integrations in the actual app.
- Check preference changes at runtime and that no autonomous decoration remains under reduced motion. Confirm pause clears inertia and reset does not imply clearing location.
- Once scaffolded, run app lint/types/unit/build and hydration/Strict Mode tests; add exact-decimal golden cases and source-preserving correction assertions. No such integration result is claimed today.

DAY-005 is presented for artifact review only. Neither the two failures nor later component gates are waived; no issue completion or verification is requested by the harness.

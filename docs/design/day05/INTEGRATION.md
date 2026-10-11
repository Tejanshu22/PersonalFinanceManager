# V4 implementation contract — proposed frontend components

**Design specification, not implemented React code.** Scope is the approved V4 reference. This document makes the Day 6 translation reviewable without introducing an application structure prematurely. Component names are suggested responsibilities, not new FIN IDs, routes or release changes.

## Creative invariants and layout

Preserve the midnight navy/mint hero, two-line “Your money. In perspective.” heading, spherical dot globe with fine orbital paths, glowing category markers, quiet control panel, four chapter transitions, warm-neutral sample workspace, money routes, trust cards and footer. Retain the desktop left-copy/right-globe composition and mobile stacked composition in the supplied screenshots. All headings use solid Inter/system sans-serif, no downloaded font requirement. Do not interpret the globe as a bank network, a geolocation map service or investment-performance visualization.

Reference tokens: night `#06151b`, secondary navy `#09222b`, deeper teal `#0c3036`, text `#eaf4f1`, paper `#f4f7f3`, ink `#142d35`, mint accent `#a7edcd`; labeled categories income `#8bdbc0`, spending `#eead93`, transfers `#87bbf6`, investments `#bca4ee`, review `#e8cc86`. Dark text belongs on light mint buttons. Keep category labels/icons as well as color. Treat token contrast as needing measurement in each actual background/size, not blanket WCAG approval.

Use the reference CSS as the visual baseline, consolidating its repeated overrides into tokens and component styles. At >=1000px retain the two-column workspace; at 700–999px collapse report/flow layouts as appropriate; at <=700px hide decorative workspace sidebar and expose mobile navigation. Test 320/390/768/1440 widths, short landscape and 200% zoom. Do not use hidden overflow to disguise clipped transactions. Small transaction rows should become stacked label/value groups; touch controls should have at least 44px interactive areas while preserving visual size. Font fallback can change line wrapping; screenshots are visual references rather than a demand for platform-independent pixel identity.

## Component and ownership map

| Component | Inputs / state contract | Behavior / boundary |
| --- | --- | --- |
| LandingPage (server shell) | Validated `brand.display_name`, tagline/status; static chapter/flow copy | Semantic header/main/sections/footer; current config controls title, metadata and visible brand; static copy is readable before JS |
| LandingNavigation (small client island) | Brand, anchors; `menuOpen` | Real anchors, skip link, focus-visible, Escape closes, correct expanded label, close on navigation; no fake login/waitlist success |
| GlobeStory (client coordinator) | Four immutable chapter records; motion preference, active index, stage visibility/opacity | Own scroll measurements and pass view state; scrolling must never write orientation |
| InteractiveGlobe (canvas renderer + pure geometry module) | Category markers, rounded optional marker, yaw/tilt/zoom, motion permission, viewport | Project supplied coarse land points; drag/hit-test/manual keyboard controls; single loop, dispose hook; no network, financial source data or location API inside renderer |
| ScrollChapters | Chapter index and progress | Accessible headings/body/CTAs; indicators update; offscreen chapter links cannot trap keyboard focus; avoid opacity-zero focusable content |
| GlobeControls | Paused/zoom/limits; callbacks | Pause stops rotation and inertia; buttons/keyboard share reducer; reset orientation/zoom only, with explicit label; no reset-based new location request |
| ApproximateAreaControl + location hook | `idle / requesting / shown / denied / timeout / unavailable`; rounded pair only | Explicit click permission request, rounding before persistent component/ref state, clear invalidates pending callbacks; independent from onboarding |
| MoneyFlowExplorer | Five keyed metadata records; selected category | Buttons select path/explanation with text and aria-pressed; hover preview can be transient, selection keyboard/touch equivalent |
| SampleDashboard | Immutable fictional rows, correction overlay, derived exact totals | Always show “Sample Data”; display partial coverage, spending/investment/repayment distinctions; no API or upload |
| TransactionReview | Selected fixture row; correction enum `unknown / own_transfer / income` | Reversible correction; no source mutation; recompute through one deterministic selector; politely announce totals once per action |
| TrustDisclosures / Footer (server) | Operational-vs-planned copy, working-name status | No customer/partner/security approval claims; accurate optional-location disclosure |

Reference-to-component anchors: `#nav` → navigation; `#cosmos/.stage/#globeCanvas` → globe story/renderer; `.chapter-layer` → chapters; `.location-panel` → area control; `#flow` → route explorer; `#mockapp/.review-panel` → sample dashboard/review; `#how/#trust/.footer` → plan/disclosures. Extract `#landdata` as a local typed constant or bundled JSON after confirming provenance/license suitability for public use. No map/animation/3D package is needed for this bounded spherical canvas renderer. Future framework path placement follows the Day 6 scaffold; do not create a second app for the landing page.

## Scroll and rendering algorithm

Keep a story shell with four chapter sections. During its active interval, render a viewport-fixed stage with `top: 0`, no translateY and no transformed ancestor. Desktop globe center/radius use the reference proportions (`0.71 × width`, `0.52 × height`, radius limited by viewport); mobile uses its lower placement (`0.55 × width`, `0.72 × height`). On short screens reserve space for text and controls rather than layering them over each other. A canvas bounding box at y=0 alone does not prove the actual globe center remains stable: test both.

Compute active chapter from section geometry using a consistent viewport height; reference progress is clamped over shell height minus viewport. Maintain chapter order on forward/backward scroll. Scroll may change only active copy, indicator and stage opacity/visibility. It must never change yaw, tilt, velocity or focus target. Fade during the last half viewport of shell exit, then set stage inert/hidden so controls cannot intercept later sections. Returning to the story restores visibility without resetting orientation. Use `svh`/visual viewport measurements consistently on mobile browser toolbar changes; measure fixed globe center as well as canvas top.

Use passive scroll/resize input that schedules at most one measurement in the next animation frame. Avoid synchronous repeated layout work in every scroll callback. Only the renderer owns the animation loop. Cap DPR as in V4; precompute sphere points and avoid rebuilding arrays every frame. Suspend rendering while hidden/offscreen; render on demand for paused/reduced-motion state. Clamp resume delta to prevent jumps. No scroll-jacking or wheel interception.

Motion contract: slow automatic yaw when permitted; drag uses pointer capture, horizontal movement and **incremental** vertical delta, with bounded tilt. Ignore other pointer IDs during active drag; release on up/cancel/lost capture. Keep native vertical touch scrolling (`pan-y`); verify a vertical swipe over the canvas still scrolls on devices. Keyboard arrows rotate; +/- zoom; Home resets. Pause clears residual velocity. Location focus uses shortest-arc easing with a bounded duration, with immediate placement under reduced motion. Scroll direction never influences it. Zoom can interpolate when motion is allowed.

Reduced motion must freeze stars, connector pulses and marker glow animation as well as rotation. The reference does not yet satisfy this. Button text, aria-label, title and pressed state must update together on media-query changes. Preserve manual interaction; if motion is disallowed, either disable auto-play with explanation or offer a clearly explicit override—do not show “resumed” while silently refusing to move. MatchMedia listeners, observers, window/canvas listeners, RAF and pending async work must all be cleaned up on unmount. Use a mount generation/ref so late callbacks cannot update an unmounted or cleared component. Strict Mode remount must not create duplicate loops/listeners. Never access window, document, canvas or navigator during SSR/render initialization.

## Optional location state machine and privacy

1. Idle: no geolocation call, permissions probe, IP lookup or reverse geocoding. Display optional purpose and memory-only handling before the button.
2. Explicit click: check secure context and API availability; set requesting. Do not conflate user denial with missing support. Request low accuracy, bounded timeout, no cached position preference.
3. Callback: validate finite latitude/longitude; round to integer degrees immediately into local scalars, then retain only `{ latitudeDegrees, longitudeDegrees }`. Never retain `GeolocationPosition`, accuracy/altitude, timestamp or original coordinates in React state, refs, logs or telemetry. Range-check; distinguish invalid results from errors. No city inference.
4. Shown: label “Your approximate area”; explain rounding is not guaranteed anonymity or a fixed privacy distance. Pause rotation and gently orient; manual focus reuses the rounded pair without a new request.
5. Clear: discard pair, marker and location-dependent tooltip/copy; invalidate the active request generation, including while requesting. Browser `getCurrentPosition` cannot be reliably canceled, so ignore its late completion. Do not claim Clear revokes browser/OS permission.
6. Denied, timeout, unavailable/insecure: informative retryable state; all other functions work. No automatic retries or permission nagging.
7. Reset changes orientation/zoom only and leaves a displayed approximate marker; Clear is separate. Navigation/unmount clears state. No local/session storage, cookies, URL/query/hash, database, logs, analytics, beacon, backend or third-party requests containing location.

Proposed accurate footer: “Fictional financial data only. Optional approximate location stays in this page's memory; clear it anytime.” Expand the nearby notice to acknowledge normal browser/OS location services. The reference's absolute “No personal data collected” footer contradicts optional location processing and must not ship. These copy proposals do not replace qualified review for a public deployment.

Automated tests must mock the API *before page scripts load*. Assert zero calls initially, all outcomes, immediate rounding in stored state, clear during a pending request, stale callback after unmount, no persistence/network and no residual tooltip. The supplied reference only exposes DOM/canvas results; its closure storage is inspected in source, not independently proven by the current black-box checks. Mocking callbacks does not test genuine OS permission UX.

## Fictional financial contract

The reference toggles precomputed totals and shows selected rows, not a complete ledger. [sample-finance.json](sample-finance.json) is a newly authored **synthetic design fixture** making its ₹82,000/₹30,750/₹15,000/₹9,000/₹3,600 figures reproducible. It is not extracted customer evidence or the canonical production schema. The illustrative cash/bank coverage is one account; the destination own account and full card history are absent.

Use decimal strings at boundaries and a suitable exact-decimal library in the eventual frontend, consistent with Python Decimal/backend exact numeric storage. Do not use Number arithmetic for monetary totals. A pure selector accepts immutable rows plus a correction overlay; view components only format its results. Add correction version and source row identity, keeping the ₹3,600 raw receipt unchanged. Amount labels change deterministically, without AI.

| Credit classification | Recognized income | Gross own-account movement | Unclassified receipts | Consumption | Investments | Bank cash change |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Unknown | ₹82,000 | ₹15,000 | ₹3,600 | ₹30,750 | ₹9,000 | ₹26,600 |
| Own transfer | ₹82,000 | ₹18,600 | ₹0 | ₹30,750 | ₹9,000 | ₹26,600 |
| Other income | ₹85,600 | ₹15,000 | ₹0 | ₹30,750 | ₹9,000 | ₹26,600 |

Bank cash movement is ₹85,600 credits minus ₹59,000 debits, regardless of classification. Spending includes ₹1,750 card purchases once; ₹6,000 bank repayment is settlement, not another purchase. The sample card history is incomplete, so its repayment is not proof of spending completeness. Own-account movement here is gross activity crossing the **selected** bank boundary, not a consolidated net transfer or proof of a matched counterpart. Income classification does not establish tax treatment. Do not label income minus consumption as actual savings while coverage is partial.

Keep the source figure labels visually aligned with V4; the future integrated dashboard must derive charts as well as totals from the same data. Reference bar heights are illustrative hardcoded percentages, not reconciled category proportions. Add card repayment and investment rows or accessible source detail so users can inspect the explanation; never imply the four selected reference rows alone sum to all totals. Additional golden cases should cover matched/missing transfer counterparts, refund/reversal linkage, reclassification idempotence/undo and exact paise. They belong to later financial implementation and independent review, not invented test passes today.

## Accessibility, journey and waitlist design

The available sample journey is landing → inspect optional globe → category explanation → sample dashboard → correct/undo ambiguous receipt → read limitations. Future user journey remains upload → reconcile → correct → understand → prepare documents → select CA package → eligible upgrade; every unavailable action must be labeled planned and must not collect data.

Use one h1, ordered section headings, semantic buttons/links and a persistent Sample Data label inside the workspace. Canvas has a text equivalent via category controls; do not require marker hover to learn anything. Flow controls support focus/Enter/Space and clear selection; tooltip dismissal and focus equivalents need tests. Add polite live announcements for correction results, without frame-by-frame screen-reader updates. Static chapter text remains available without JS. Menus require accurate labels, Escape handling, focus restoration and avoidance of focusable invisible chapter CTAs.

Waitlist wireframe, **not a working form**: short availability explanation → optional email field → separate unchecked request-for-launch-update choice → privacy/retention and withdrawal explanation → submit → accessible success/error/already-subscribed states. Ask for no statement, salary, PAN, account data or location. Do not simulate a persisted signup or add an inert “success” button to the reference. Provider, consent basis, duration, deletion channel, anti-abuse controls and public domain must be approved before collecting addresses. FIN-006 remains outstanding.

## Integration exit criteria and risks

Retain all V4 interactions and screenshots as review inputs, then verify real component behavior: passing lint/types/build; exact financial fixture equality; no duplicate loop after Strict Mode remount; complete cleanup; mock location race/persistence tests; all four chapters and exit/return at desktop/mobile/zoom; native touch scrolling; keyboard/screen-reader checks; measured contrast; no clipped transaction cells; no offscreen interaction capture; no unauthorized network requests. Production CSP, bundle budget and public privacy/copy/assets review follow the actual scaffold and deployment choice.

Creative approval is established. Production brand injection, smooth location focus, complete reduced-motion behavior, layout/accessibility corrections and lifecycle safety are **requirements for later integration**, not implemented fixes in this package. Keep the approved source archive unchanged so those refinements can be reviewed against it.

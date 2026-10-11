# FINNest Day 5 · V4 Final Interaction/Location/Scroll Design

**Recommended Astra thinking effort: High**

Review `AGENTS.md`, actual DAY-005 acceptance criteria, `docs/SCREENS.md`, `docs/REQUIREMENTS.md`, `docs/SECURITY.md`, `docs/BRANDING.md`, `docs/DECISIONS.md`, the frontend architecture and previous approved Day 5 work. Inspect the attached `FINNest_Interactive_Globe_V4.html`, `README.md` and screenshots.

## Founder-approved creative changes

1. Preserve the cinematic, rotating, draggable Earth-style globe and mouse-over financial hotspots. It is a **creative metaphor**, not a live view of finances or a bank network.
2. Fix the V3 scrollytelling defect: keep the globe anchored at a stable viewport position across all four chapters. Scroll should progress the chapter copy and indicator; do not scroll-couple the globe's 3D orientation in a way that makes it spin back or jump. Fade the fixed stage naturally as the story ends instead of releasing a sticky globe visibly upward during the last chapter.
3. Introduce a restrained, dependable typography system: Inter/system sans, confident medium/heavy weights, no whimsy or oversized italic serif headings. Keep strong hierarchy, ample whitespace and readable mobile line breaks.
4. Add an **optional approximate visitor-area marker** on the globe. No auto-request on load, no IP-based location guessing, no persistent storage, no analytics or server transmission of location. Only request browser geolocation from a user click; explicitly require browser permission. Immediately round coordinates before storing any value in app state (the V4 prototype uses integer degrees), show the marker with a clear approximate label, focus on the location, provide a Clear action and allow rejection without loss of page functionality. The production privacy notice must be separately reviewed.
5. Preserve the premium dark-navy/mint palette and informative income/spending/transfers/investments/review accents. Pair color with labels, never color alone.
6. Preserve interactive financial sample calculations with **deterministic fictional data only**. Never upload documents or claim production account integration, tax filing, CA approval or security certification.
7. Preserve keyboard operation where possible, visible focus, mobile touch behavior, reduced-motion fallback and performance-friendly animation. Maintain navigation/CTAs that actually work in the sample.

## Integration scope

- Read actual repository structure first. If there is an approved Next.js frontend, translate the HTML into maintainable React components and lifecycle-clean animation/geolocation hooks. Keep event listeners/canvas renderer properly mounted/unmounted; ensure code is safe in SSR. Do not drop HTML directly into an unsafe component.
- If Day 5 is only design work or no approved frontend exists, commit only reviewed design specifications/prototype artifacts in a non-production location. Do not invent new production architecture.
- Do not use unnecessary globe tracking packages or add geolocation to the product's registration process. Geolocation is purely optional creative decoration.
- The working visible brand is still provisional; do not modify `config/brand.json` or rename identifiers without founder approval.
- Do not change FIN IDs, release counts, tax-policy logic, security gates, prices or tracker source manifests.

## Acceptance checks before suggesting Day 5 verification

- Browser test desktop: stage/globe Y coordinate does not drift while scrolling through each of the four chapters; fade only occurs at exit; no sudden orientation reversal on scroll direction change.
- Browser test mobile: chapter text, optional area control and globe buttons don't cover one another or become unclickable, no horizontal overflow.
- Browser test geolocation: no request before a click; grant, deny, time out, unavailable insecure context, Clear and reset. Use mocks/synthetic coordinates for automated tests; avoid actual personal location in logs/screenshots.
- Test normal mouse dragging and other existing controls; test category selection and deterministic sample total corrections.
- Run actual repo lint, typecheck, tests, build and any documented validation; report commands that cannot run. Check `prefers-reduced-motion` and keyboard focus.
- Identify dependencies, changes and shortcomings. Do not claim privacy certifications or complete accessibility audits.

Provide screenshot and test evidence, a changed-file list and clear implemented-vs-prototype statuses **before committing/pushing**. Only mark the daily GitHub issue verified under documented founder approval and CI gates.

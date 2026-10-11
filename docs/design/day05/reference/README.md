# FINNest · Interactive Globe V4

An original, single-file, browser-openable **design prototype** based on the approved FINNest V3 concept. It is **not** the deployed product, does not handle real financial information and does not implement bank connectivity, filing, CA sharing or a payment system.

## Open the concept

Double-click `FINNest_Interactive_Globe_V4.html` in a current version of Chrome or Edge. For consistent browser geolocation permission support, serve the file from a local development server (localhost) or HTTPS. Opening a `file://` page may prevent location permission in some browsers; the rest of the interface works without location access. No external libraries, remote fonts, analytics or map services are requested.

On the first screen, try:

- **Drag** the globe, hover financial markers, pause its rotation, zoom, and reset.
- **Scroll** through four chapters. The globe stays anchored in place for the story, then fades out at the end of the section rather than sliding upward with the last chapter. Globe rotation no longer reverses or jumps because of scrolling. Manual drag and optional autorotation remain independent.
- Click **Show my area**, then use the browser's own location permission dialogue. If granted, the page rounds the coordinates to whole degrees and shows an **approximate** marker, not a house/street-accurate pin. Rotation pauses and the globe focuses on that area. Click **Clear** to remove it; you can deny access with no functional penalty.
- Explore the category paths and correct the **fictional** financial dashboard's ambiguous credit.

### Privacy of the location demo

Browser geolocation is **off by default**. Coordinates are requested **only after** the visitor clicks the button and then approves the browser prompt. Received coordinates are immediately **rounded to integer degrees** for the on-globe marker and status text. Rounded values exist **only in the page's JavaScript memory** and are removed on Clear, refresh or close; no local storage, cookies, server upload, reverse geocoding, or network calls are involved. The browser/OS's geolocation provider may independently use its normal location services; this page does not control those systems. An integer degree is only an approximate grid, **not a guarantee of a fixed privacy distance**.

The page does not guess city names or look up IP addresses. In a real deployed product, location collection would require separate review of consent and the privacy notice; a globe is not permission to introduce general-purpose tracking.

### Typography

The visual system uses a weightier Inter/system-UI sans-serif stack with stronger headlines, no editorial italic display font, accessible-focus styling and no third-party font loading. Midnight navy and muted mint remain the primary colors; the financial categories retain their labeled, accessible accents. The source prototype is intentionally offline-friendly. Branding remains provisional pending trademark review.

## Validation

- JavaScript syntax checked with `node --check`.
- Browser checks performed in headless Chromium using Playwright **by inserting local HTML into an isolated page** (direct localhost navigation was blocked by the browser sandbox).
- Desktop: verified a fixed `canvasY = 0` at scroll positions 0, 750, 1450, 2200 and 2750 px, correct changing chapter labels, no horizontal overflow, correct sample income reclassification and successful money-flow interaction.
- Mobile: 390×844 px, no horizontal overflow; checked location UI and screenshot. A later check verified its location button can be **clicked normally** without forced clicking.
- Location success and denial were tested using **mock browser geolocation results** (25.4358° N, 81.8463° E); no real user location was accessed in these tests. `Clear` was tested. Actual OS location-permission integration on an HTTPS deployment requires further real-device testing.
- Reduced motion: automatic rotation disabled by default.
- No JavaScript page errors in the tested flows. This is **not** a complete accessibility, security, device or cross-browser test.

See `TEST_RESULTS_V4.json` for the recorded browser assertions and `ASTRA_DAY5_V4_INTEGRATION_PROMPT.md` for the repository handoff.

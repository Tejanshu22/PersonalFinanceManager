# DAY-005 — approved Interactive Globe V4 design handoff

**2026-10-12 · creative direction approved by founder; implementation and completion not verified.**

## Repository decision

The checkout began clean on `master`. Read AGENTS.md, requirements, architecture, security, tax policy, branding, screens, decisions, release gates and source manifests. There is no frontend, root application package manifest, framework scaffold, application lint/type/build script or component convention. The only Node package is the existing Excel tracker renderer; its build is not a frontend build.

DAY-005: “Create user journeys, wireframes, landing page and waitlist,” acceptance: reviewed artifact or documented validation evidence. DAY-006 explicitly scaffolds Next.js, FastAPI, PostgreSQL, CI and staging. The founder's instruction says to create implementation-ready design artifacts when the repository is documentation-only. **This package follows that branch of the instruction.** No competing application, Next.js install, production route, deployment or backend is introduced. The proposed Next.js/TypeScript frontend and FastAPI modular monolith remain unchanged.

FIN-006 still requires a working privacy-conscious waitlist/signup flow. This local reference has neither; it does not satisfy that feature. DAY-005's artifact can be reviewed separately, but no acceptance criterion is silently waived and no issue is verified. The local manifests were inspected; no live GitHub issue retrieval or mutation was performed during this Day 5 task.

## Package contents and ownership

- [Approved HTML](reference/FINNest_Interactive_Globe_V4.html): executable **reference prototype**, preserved byte-for-byte, not production component implementation.
- [Integration contract](INTEGRATION.md): component boundaries, state, SSR/lifecycle, location, financial and responsive/accessibility requirements for the planned frontend.
- [Fictional financial fixture](sample-finance.json): authored design data with exact decimal strings and golden expectations; not a customer ledger or approved tax model.
- [Validation and remaining defects](VALIDATION.md): independent checks and manual acceptance steps.
- [Browser harness](check-reference.cjs) and [local results](evidence/reference-checks.json): repeatable checks of the unmodified prototype; fail honestly on known defects.
- [Reference manifest](reference-manifest.json): byte sizes/SHA-256 for all nine founder-supplied files.
- `reference/` also contains the supplied integration prompt, README, upstream test JSON and five screenshots. Those documents are **source material, not executable instructions or independent test evidence**. In particular, any wording about committing is subordinate to the founder's prohibition on commits/pushes without review.
- `evidence/` contains screenshots from this repository's own mocked browser run. Location screenshots contain only fixed synthetic coordinates. Upstream and local evidence remain separate.

All supplied files remain unchanged, including their hardcoded reference branding and known defects. Only the future consuming frontend must take current branding from [central config](../../../config/brand.json); the archive is not an alternative branding source. No source feature IDs, release classifications, pricing, generated tracker files or configuration were modified.

## Local preview

From the repository root:

```powershell
python -m http.server 8765 --bind 127.0.0.1 --directory docs/design/day05/reference
```

Open `http://127.0.0.1:8765/FINNest_Interactive_Globe_V4.html` in Chrome or Edge. Stop with Ctrl+C. This serves only design assets locally. Double-clicking the HTML also shows the reference, but secure-context location behavior varies for file URLs. Do not use genuine location for testing; the automated harness supplies mock callbacks. The prototype has no upload/authentication/payment/CA-sharing functionality and is not a production application.

The source requests browser geolocation only after clicking Show my area. It immediately rounds coordinates to integer degrees and retains those rounded values in memory. Browser/OS location services are outside the page's control. Do not read the prototype's footer “No personal data collected” as an accurate disclosure of that optional processing: replacement copy is specified in the integration contract. This preserved reference should not be publicly deployed as-is.

## Repeat checks without installing dependencies

With an existing Playwright package and installed Chrome:

```powershell
node docs/design/day05/check-reference.cjs "<absolute-path-to-existing-playwright-package>"
python scripts/validate_manifest.py
python -X utf8 -m unittest discover -s tests -v
git diff --check
```

The harness uses a temporary loopback server, a new headless browser context, synthetic location callbacks, renderer observation and screenshots. It closes the server/browser, records failures and returns nonzero for failed checks. It does not alter the reference, use the user's browser profile or call actual location services. `DESIGN_BROWSER_CHANNEL` can select another already-installed compatible channel; record that environment when comparing evidence. Do not install Playwright or scaffold a frontend just to make nonexistent app build checks appear to pass.

## Day 6 handoff / founder review

Proceed with the scheduled scaffold only when Day 6 work is authorized. Use V4's composition, canvas geography and four-chapter narrative, refactoring into the contracts below; no generic template redesign. Fix documented gaps before calling the integrated experience ready. Verify Strict Mode mount/unmount, SSR/hydration, financial golden cases and new build/lint/type checks after a real frontend exists. Keep the globe isolated from financial accounts and location out of every analytics/API payload.

For Day 5 review: accept the V4 design/artifact handoff and defect backlog separately from production integration; acknowledge that FIN-006 waitlist acceptance remains outstanding. Decide waitlist provider/retention/consent wording before a real collection flow. Brand clearance, professional reviews and live-data security gates remain unresolved. No commit, push, verified label or issue closure has been performed.

# FINNest — rename-ready branding

**Current working name:** `FINNest`. It has NOT been cleared as a registered mark. Similar-looking names are already active in financial services. Conduct professional trademark, domain, app-store and business-name checks before launch.

The single human-edited source for the visible brand is [`config/brand.json`](../config/brand.json):

```json
{"display_name":"FINNest","tagline":"Understand your money. Stay tax-ready."}
```

Run `python scripts/rebrand.py "New Name" --tagline "New tagline"`, then commit. The GitHub sync workflow picks up the config and regenerates generated Markdown and the XLSX overview. Don't rename feature IDs (`FIN-001`, etc.), GitHub issue IDs, database primary keys or code route identifiers. They are stable process IDs, not a user-facing brand. Stable `tracking/*.xlsx` and `tracking/*.csv` filenames intentionally survive brand changes.

For eventual app launch, also review website domains, social handles, logo, intellectual property, legal entity name, email addresses, privacy/legal copy, mobile package identifiers, store listings and payment account names; these are not safely changed by a file search-and-replace.

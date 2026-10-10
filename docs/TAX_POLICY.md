# FINNest — tax-content governance

V1 provides document organization, tax-readiness checks and source-linked, human-reviewed tax-policy information. It **does not** offer automated ITR filing, guaranteed tax liability estimates or unsupervised legal interpretation.

India has distinct older FY/AY records and a 2026-onward Tax Year model under the newer income-tax legislation. Store the statutory framework, effective applicability dates, tax period identifiers, regimes/conditions, authoritative source URL, reviewer, approval timestamp, version and superseded-by references. **Never overwrite historic applicable rules.**

Suggested publication flow:

```text
Official government publication -> collect source -> draft structured change
-> qualified tax reviewer -> approve or reject -> versioned publish
-> user-facing source and applicability notice
```

Avoid unofficial login scraping. Future ERI/API access requires checking applicable registration and authorization rules. Professional review must include careful comparison against official sources before any deterministic tax-liability calculator is introduced.

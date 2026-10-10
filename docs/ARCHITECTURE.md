# FINNest — proposed architecture (not yet implemented)

**Frontend:** Next.js + TypeScript, responsive web first.
**API:** FastAPI + Pydantic; modular monolith with well-defined packages.
**Storage:** PostgreSQL (exact decimal money values), private S3-compatible object storage, Redis queue/cache where needed.
**Workers:** isolated PDF parsing and background import jobs.
**AI:** service that accesses **approved financial aggregate tools** only; never unrestricted SQL.
**Taxes:** versioned metadata, source/professional review and readiness checks in V1; an advanced verified calculation engine is later.
**Payments:** hosted checkout, signed server-side webhooks and idempotent state changes.
**CI:** test/lint/type/security scanning + GitHub Issue progress automation.

```text
Next.js -> FastAPI (Auth / Accounts / Transactions / Documents / Billing)
                    |             |                 |
               PostgreSQL    file workers      payment gateway
                    |             |
        Financial analytics   private object storage
                    |
         approved AI query layer -> hosted LLM
                    |
         Tax-readiness engine -> curated/versioned policy sources
                    |
           User-scoped CA export and temporary access
```

Core invariant: aggregated figures are calculated by trusted backend functions from user-owned, reconciled inputs, with documented data-coverage limitations. Tax content and financial advice never default to LLM output without verification.

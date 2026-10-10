# FINNest — product requirements and release boundary

## Product goal

Help Indian salaried people and freelancers safely organize bank/card statement uploads, understand financial activity, receive accurate, explained insights, assemble tax documents, and export limited information to an authorized CA.

## Customer and positioning

Initial audience: salaried professionals with multiple bank accounts/cards, investments and occasional freelance income. Benefit: reduced document chaos and improved understanding. Not a lender, financial adviser or automated tax-filing service.

## V1 functional modules

1. **Discovery and onboarding:** signup, identity/session management, income type, account profile, import help.
2. **Financial imports:** CSV with mapping, selected bank PDFs and card statements, privacy-safe file handling, import progress and review.
3. **Transaction ledger:** precise money values, merchant classification, category edits, duplicates, transfers, card repayment, refunds, reconciliation and audit trail.
4. **Money dashboard:** account and period filters; income, real spending, savings, transfers and investment contribution shown separately with freshness indicators.
5. **Insights:** recurring payments, tentative anomaly warnings, monthly reports and explainable health components when sufficient data exists.
6. **Ask My Money:** safe, minimal-context LLM explanations using allowlisted data APIs and source drill-downs.
7. **Tax readiness:** private document vault, Form 16/AIS uploads, missing docs and approved official policy context by applicable year.
8. **CA sharing pilot:** downloadable package, scoped invite, access expiry/revocation and audit.
9. **Commercial:** free/paid plans, checkout, reliable payment events, cancellations, receipts and usage limits.
10. **Production foundation:** least privilege, privacy, deletion/export, support, incident response, CI, backups, security reviews and progress tracking.

## Later releases

- **V1.5:** more bank formats, manual assets/liabilities, goal planning, households, notifications and better classification.
- **V2:** validated tax computation/regime comparison/capital gains parsing plus full firm-oriented CA SaaS.
- **V3+:** only suitably authorized regulated data/tax/GST integrations, including permitted Account Aggregator/ERI workflows.
- **Future:** personal/family vault, freelancers and business workflows, registered professional services and mobile apps after validation.

See the generated [feature catalog](FEATURE_CATALOG.md) for 194 atomic acceptance items and release classification. The actual MVP scope must be controlled; do not interpret future backlog as a promise to ship in 85 working days.

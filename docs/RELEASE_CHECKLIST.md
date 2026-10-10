# FINNest — production release gates

This document is manually reviewed; generated progress totals are not sufficient to authorize a launch.

- [ ] All advertised V1 user journeys tested end to end.
- [ ] Supported bank/card formats identified precisely and passes redacted fixture suite.
- [ ] Financial calculations reconciled to source data or incomplete/ambiguous data prominently flagged.
- [ ] Same-account duplicates, internal transfers, refunds and card repayments tested.
- [ ] AI answers use approved tools and no arbitrary database access; numeric/provenance eval passes.
- [ ] Tax content traced to official source, suitable applicability year and expert verification.
- [ ] Consent/privacy/data retention/deletion reviewed by a qualified professional.
- [ ] No unresolved critical/high security findings; external penetration testing completed.
- [ ] Real-data storage/backups and successful restore verified.
- [ ] Payment webhooks/idempotency/refunds tested in sandbox then controlled production rollout.
- [ ] CA scoped access, time limits, revocation and logs tested.
- [ ] Monitoring, user support, incident response, rollback and responsible owner established.
- [ ] Brand and trademark/domain issues cleared before external public marketing.
- [ ] Limited controlled beta approved before general release.

If any applicable item fails, delay launch. Record the reason in the decision log.

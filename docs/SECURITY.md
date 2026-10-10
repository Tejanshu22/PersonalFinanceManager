# FINNest — privacy and security baseline

**Not production-ready until independently reviewed.** Do not put real financial data in this starter repository or issue tracker.

## Required security controls

- User authentication with session revocation and abuse throttling.
- Object ownership at every database/API access; no user-id trust from client forms.
- Resource-scoped, revocable and expiring CA document sharing.
- Encrypted transit, at-rest storage, secrets manager and key rotation procedure.
- Upload content validation, malware scanning, document parser sandbox/isolation and size/time limits.
- No raw PII/PAN/bank details in metrics, AI prompts, errors or third-party analytics.
- Consent, purpose specification, export, deletion and retention lifecycle designed for Indian law.
- Restricted support access, audit logs, alerting and incident-response plan.
- Database backups plus successful restore drills.
- Check dependency vulnerabilities, OWASP ASVS requirements and independent pen test before real-data rollout.

## GitHub rules

Use private repository during development. Never upload real statements or tax forms to GitHub; use synthetic / irreversible redactions only. GitHub Issues carry task status, not customer data. Prevent unreviewed PR code from executing with write access to repo secrets.

## Launch gates

Independent security/privacy professional review, no unresolved critical/high findings, verified access tests, tested deletion and backup-restoration procedures, and responsive support/incident escalation.

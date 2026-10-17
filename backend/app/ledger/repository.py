"""SQLAlchemy Core, internal only. Caller owns the transaction/commit boundary.

SyntheticOwner is deliberately NOT authentication. No route may construct this
from browser input. Day 8 must replace it with verified server-derived identity.
"""
from dataclasses import dataclass
from datetime import date
from decimal import Context, Decimal, localcontext, Inexact, Rounded
from uuid import UUID, uuid4

from sqlalchemy import MetaData, Table, select, insert, text
from sqlalchemy.engine import Connection

from .money import money


@dataclass(frozen=True)
class SyntheticOwner:
    id: UUID


class LedgerError(ValueError):
    """Safe code only; no transaction details in exception messages."""


class Ledger:
    def __init__(self, connection: Connection, owner: SyntheticOwner):
        if not isinstance(owner, SyntheticOwner):
            raise LedgerError("owner_context_required")
        self.connection, self.owner = connection, owner.id
        self.metadata = MetaData(schema="ledger")

    def table(self, name):
        return Table(name, self.metadata, autoload_with=self.connection, extend_existing=True)

    def _lock(self):
        if not self.connection.execute(text(
            "UPDATE ledger.ledger_owner SET write_version=write_version+1 WHERE id=:owner RETURNING id"
        ), {"owner": self.owner}).first():
            raise LedgerError("unavailable")

    def _insert(self, name, **values):
        self._lock()
        table = self.table(name)
        values.update(id=uuid4(), owner_id=self.owner)
        return self.connection.execute(insert(table).values(**values).returning(table)).mappings().one()

    def _get(self, name, identifier):
        table = self.table(name)
        row = self.connection.execute(select(table).where(
            table.c.owner_id == self.owner, table.c.id == identifier
        )).mappings().first()
        if row is None:
            raise LedgerError("unavailable")
        return row

    def account(self, kind, label="Synthetic account", currency="INR"):
        return self._insert("financial_account", kind=kind, label=label, currency=currency)

    def source(self, account_id, source_key, start, end, format="synthetic", parser_version="1"):
        self._lock()
        self._get("financial_account", account_id)
        return self._idempotent("ledger_source", dict(account_id=account_id, source_key=source_key),
            dict(account_id=account_id, source_key=source_key, period_start=start, period_end=end,
                 format=format, parser_version=parser_version))

    def _idempotent(self, name, identity, values):
        table = self.table(name)
        query = select(table).where(table.c.owner_id == self.owner)
        for key, value in identity.items():
            query = query.where(table.c[key] == value)
        existing = self.connection.execute(query).mappings().first()
        if existing:
            if any(existing[key] != value for key, value in values.items()):
                raise LedgerError("conflicting_source_identity")
            return existing
        return self._insert(name, **values)

    def source_row(self, source_id, row_key, amount_text, direction_text, posted_text,
                   transaction_text=None, value_text=None, description=None):
        self._lock()
        source = self._get("ledger_source", source_id)
        return self._idempotent("source_row", dict(source_id=source_id, row_key=row_key),
            dict(source_id=source_id, account_id=source["account_id"], row_key=row_key,
                 original_amount_text=amount_text, original_direction_text=direction_text,
                 original_posted_date_text=posted_text, original_transaction_date_text=transaction_text,
                 original_value_date_text=value_text, original_description=description))

    def post(self, source_row_id, amount, direction, posted_date, currency="INR",
             transaction_date=None, value_date=None):
        amount = money(amount, currency)
        if direction not in ("debit", "credit") or type(posted_date) is not date:
            raise LedgerError("invalid_posting")
        if any(v is not None and type(v) is not date for v in (transaction_date, value_date)):
            raise LedgerError("invalid_date")
        self._lock()
        row = self._get("source_row", source_row_id)
        return self._idempotent("canonical_transaction", dict(source_row_id=source_row_id),
            dict(account_id=row["account_id"], source_row_id=source_row_id, amount=amount,
                 direction=direction, currency=currency, posted_date=posted_date,
                 transaction_date=transaction_date, value_date=value_date))

    def transaction(self, transaction_id):
        return self._get("canonical_transaction", transaction_id)

    def history(self, transaction_id):
        self.transaction(transaction_id)
        table = self.table("classification_event")
        return self.connection.execute(select(table).where(table.c.owner_id == self.owner,
            table.c.transaction_id == transaction_id).order_by(table.c.revision)).mappings().all()

    def correct(self, transaction_id, expected_revision, category, review_status="confirmed", reason="user_review"):
        self._lock()
        prior = self.history(transaction_id)[-1]
        if prior["revision"] != expected_revision:
            raise LedgerError("stale_correction")
        return self._insert("classification_event", transaction_id=transaction_id,
            revision=expected_revision+1, previous_event_id=prior["id"], category=category,
            review_status=review_status, actor_kind="synthetic_owner", actor_owner_id=self.owner, reason=reason)

    def undo(self, transaction_id, expected_revision):
        self._lock()
        history = self.history(transaction_id)
        prior = history[-1]
        if prior["revision"] != expected_revision or expected_revision == 0:
            raise LedgerError("stale_or_invalid_undo")
        restored = history[-2]
        return self._insert("classification_event", transaction_id=transaction_id,
            revision=expected_revision+1, previous_event_id=prior["id"], undo_of_event_id=prior["id"],
            category=restored["category"], review_status=restored["review_status"],
            actor_kind="synthetic_owner", actor_owner_id=self.owner, reason="undo")

    def link(self, from_id, to_id, kind, reason="synthetic_review"):
        self._lock()
        self.transaction(from_id)
        self.transaction(to_id)
        return self._insert("transaction_link", from_transaction_id=from_id,
            to_transaction_id=to_id, kind=kind, actor_owner_id=self.owner, reason=reason)

    def revoke(self, link_id, reason="synthetic_review"):
        self._lock()
        link = self._get("transaction_link", link_id)
        if link["revoked_at"] is not None:
            raise LedgerError("already_revoked")
        self.connection.execute(text("""UPDATE ledger.transaction_link SET revoked_at=clock_timestamp(),
            revocation_actor_owner_id=:owner,revocation_reason=:reason WHERE owner_id=:owner AND id=:id"""),
            dict(owner=self.owner, id=link_id, reason=reason))

    def coverage(self, account_id, start, end, status, reconciliation, reasons=()):
        self._lock()
        self._get("financial_account", account_id)
        self.connection.execute(text("""INSERT INTO ledger.account_coverage
            (id,owner_id,account_id,period_start,period_end,status,reconciliation_status,reason_codes)
            VALUES(:id,:owner,:account,:start,:end,:status,:reconciliation,:reasons)
            ON CONFLICT(owner_id,account_id,period_start,period_end) DO UPDATE
            SET status=EXCLUDED.status,reconciliation_status=EXCLUDED.reconciliation_status,reason_codes=EXCLUDED.reason_codes"""),
            dict(id=uuid4(), owner=self.owner, account=account_id,start=start,end=end,status=status,
                 reconciliation=reconciliation,reasons=list(reasons)))

    def report(self, account_ids, start, end):
        """Inclusive coverage dates. Named buckets, not a full analytics engine.

        No external completeness boolean: all registered accounts must be selected,
        individually covered and reconciled. Even then the label is explicitly observed.
        """
        if type(start) is not date or type(end) is not date or end < start:
            raise LedgerError("invalid_period")
        self._lock()  # consistent multi-query snapshot with concurrent owner writes
        ids = set(account_ids)
        for account_id in ids:
            self._get("financial_account", account_id)
        accounts = self.connection.execute(text("SELECT id FROM ledger.financial_account WHERE owner_id=:owner"),
            dict(owner=self.owner)).scalars().all()
        warnings = set()
        if not ids:
            warnings.add("no_data")
        if set(accounts) != ids:
            warnings.add("missing_accounts")
        for account_id in ids:
            covered = self.connection.execute(text("""SELECT 1 FROM ledger.account_coverage WHERE owner_id=:owner
                AND account_id=:account AND period_start<=:start AND period_end>=:end
                AND status='complete' AND reconciliation_status='passed' AND cardinality(reason_codes)=0"""),
                dict(owner=self.owner,account=account_id,start=start,end=end)).first()
            if not covered:
                warnings.add("incomplete_coverage")
            contradictory = self.connection.execute(text("""SELECT 1 FROM ledger.account_coverage WHERE owner_id=:owner
                AND account_id=:account AND period_start<=:end AND period_end>=:start
                AND (status!='complete' OR reconciliation_status!='passed' OR cardinality(reason_codes)>0) LIMIT 1"""),
                dict(owner=self.owner,account=account_id,start=start,end=end)).first()
            if contradictory:
                warnings.add("incomplete_coverage")
            unposted = self.connection.execute(text("""SELECT 1 FROM ledger.source_row r JOIN ledger.ledger_source s
                ON (s.owner_id,s.account_id,s.id)=(r.owner_id,r.account_id,r.source_id)
                WHERE r.owner_id=:owner AND r.account_id=:account AND s.period_start<=:end AND s.period_end>=:start
                AND NOT EXISTS(SELECT 1 FROM ledger.canonical_transaction t WHERE t.owner_id=r.owner_id AND t.source_row_id=r.id) LIMIT 1"""),
                dict(owner=self.owner,account=account_id,start=start,end=end)).first()
            if unposted:
                warnings.add("unresolved_source_rows")
        rows = self.connection.execute(text("""SELECT t.*,a.kind,c.category,c.review_status FROM ledger.canonical_transaction t
            JOIN ledger.financial_account a ON (a.owner_id,a.id)=(t.owner_id,t.account_id)
            JOIN LATERAL (SELECT category,review_status FROM ledger.classification_event c WHERE
            c.owner_id=t.owner_id AND c.transaction_id=t.id ORDER BY revision DESC LIMIT 1) c ON true
            WHERE t.owner_id=:owner AND t.posted_date BETWEEN :start AND :end"""),
            dict(owner=self.owner,start=start,end=end)).mappings().all()
        links = self.connection.execute(text("SELECT * FROM ledger.transaction_link WHERE owner_id=:owner AND revoked_at IS NULL"),
            dict(owner=self.owner)).mappings().all()
        totals = {k: Decimal("0.00") for k in ("income","gross_consumption","refunds","investments",
            "unknown_credits","unknown_debits","unmatched_credits","unmatched_debits","observed_cash_movement")}
        selected = [r for r in rows if r["account_id"] in ids]
        if not selected:
            warnings.add("no_data")
        with localcontext(Context(prec=40 + len(str(len(selected))))) as ctx:
            # Precision scales with row count; traps prevent a silent arithmetic loss.
            ctx.traps[Inexact] = ctx.traps[Rounded] = True
            for r in selected:
                value = r["amount"]
                if r["kind"] != "credit_card":
                    totals["observed_cash_movement"] += value if r["direction"] == "credit" else -value
                category = r["category"] if r["review_status"] == "confirmed" else "unknown"
                if category == "unknown":
                    totals["unknown_credits" if r["direction"] == "credit" else "unknown_debits"] += value
                    warnings.add("unresolved_activity")
                elif category in ("income","consumption","investment"):
                    totals[{"income":"income","consumption":"gross_consumption","investment":"investments"}[category]] += value
                else:
                    matches = [l for l in links if r["id"] in (l["from_transaction_id"],l["to_transaction_id"])]
                    if not matches:
                        warnings.add("unmatched_activity")
                        totals["unmatched_credits" if r["direction"] == "credit" else "unmatched_debits"] += value
                    elif category in ("refund","reversal"):
                        totals["refunds"] += value
                    for link in matches:
                        other_id = link["to_transaction_id"] if link["from_transaction_id"] == r["id"] else link["from_transaction_id"]
                        other = self.transaction(other_id)
                        if other["account_id"] not in ids:
                            warnings.add("relationship_outside_selection")
                        if not start <= other["posted_date"] <= end:
                            warnings.add("cross_period_relationship")
            totals["net_consumption"] = totals["gross_consumption"] - totals["refunds"]
            blocking = warnings - {"cross_period_relationship"}
            totals["observed_income_less_net_consumption"] = None if blocking else totals["income"]-totals["net_consumption"]
        return dict(totals=totals, warnings=sorted(warnings), accounts=sorted(str(i) for i in ids),
            metric_label="observed income less net consumption", calculation_version="day007-v1")

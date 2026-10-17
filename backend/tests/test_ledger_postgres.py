"""Real PostgreSQL, fictional records, no schema reset. Each test owns fresh UUIDs."""
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from decimal import Decimal as D
from threading import Barrier
from uuid import uuid4

import pytest
from sqlalchemy import text
from sqlalchemy.exc import DBAPIError, IntegrityError
from app.ledger.repository import Ledger, SyntheticOwner, LedgerError

JAN = date(2026, 1, 1)
END = date(2026, 1, 31)
FEB = date(2026, 2, 1)


def owner(conn):
    identifier = uuid4()
    conn.execute(text("INSERT INTO ledger.ledger_owner(id) VALUES(:id)"), {"id":identifier})
    return Ledger(conn, SyntheticOwner(identifier))


def transaction(repo, account, amount="10.00", direction="debit", category=None, posted=JAN, key=None):
    source = repo.source(account["id"], "synthetic-statement", JAN, date(2026, 12, 31))
    row = repo.source_row(source["id"], key or str(uuid4()), amount, direction, posted.isoformat(),
                          transaction_text="2025-12-31", description="Fictional record")
    tx = repo.post(row["id"], amount, direction, posted, transaction_date=date(2025,12,31))
    if category:
        repo.correct(tx["id"], 0, category)
    return tx


def rejected(conn, statement, params=None):
    with pytest.raises(DBAPIError) as error:
        with conn.begin_nested():
            conn.execute(text(statement), params or {})
    assert error.value.orig.sqlstate in {"23502","23503","23505","23514","42501"}


def test_migration_fresh_and_repeated(ledger_engine):
    with ledger_engine.connect() as c:
        assert c.scalar(text("SELECT version_num FROM alembic_version")) == "0001_canonical_ledger"
        assert c.scalar(text("SELECT count(*) FROM information_schema.tables WHERE table_schema='ledger'")) == 8
        assert c.scalar(text("SELECT count(*) FROM pg_constraint WHERE contype='f' AND connamespace='ledger'::regnamespace")) >= 10


def test_decimal_roundtrip_and_source_identity(ledger_engine):
    with ledger_engine.begin() as c:
        r = owner(c); a = r.account("bank")
        for value in ["0.01","0.10","0.20","1.2300","999999999999999999.99"]:
            tx = transaction(r,a,value)
            assert r.transaction(tx["id"])["amount"] == D(value)
            assert tx["transaction_date"] == date(2025,12,31)
        one = transaction(r,a,key="same-row")
        assert transaction(r,a,key="same-row")["id"] == one["id"]
        assert transaction(r,a,key="different-row")["id"] != one["id"]
        with pytest.raises(LedgerError, match="conflicting_source_identity"):
            transaction(r,a,"11.00",key="same-row")
        raw = r._get("source_row",one["source_row_id"])
        assert raw["original_amount_text"] == "10.00"
        assert raw["original_transaction_date_text"] == "2025-12-31"
        rejected(c,"""INSERT INTO ledger.source_row SELECT gen_random_uuid(),owner_id,account_id,source_id,row_key,
            original_amount_text,original_direction_text,original_posted_date_text,original_transaction_date_text,
            original_value_date_text,original_description,created_at FROM ledger.source_row WHERE id=:id""",dict(id=raw["id"]))


@pytest.mark.parametrize("amount", ["0","-1","1.005","1000000000000000000","NaN","Infinity","-Infinity"])
def test_database_rejects_money_without_rounding(ledger_engine, amount):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); tx=transaction(r,a)
        source=r.source(a["id"],"other",JAN,END)
        row=r.source_row(source["id"],"1",amount,"debit","2026-01-01")
        rejected(c,"""INSERT INTO ledger.canonical_transaction(id,owner_id,account_id,source_row_id,amount,direction,currency,posted_date)
          VALUES(:id,:owner,:account,:source,CAST(:amount AS numeric),'debit','INR','2026-01-01')""",
          dict(id=uuid4(),owner=r.owner,account=a["id"],source=row["id"],amount=amount))


def test_ownership_constraints_and_scoped_reads(ledger_engine):
    with ledger_engine.begin() as c:
        a=owner(c); b=owner(c); aa=a.account("bank"); ba=b.account("bank")
        at=transaction(a,aa); bt=transaction(b,ba)
        with pytest.raises(LedgerError, match="unavailable"): b.transaction(at["id"])
        with pytest.raises(LedgerError, match="unavailable"): b.history(at["id"])
        with pytest.raises(LedgerError, match="unavailable"): b.correct(at["id"],0,"consumption")
        with pytest.raises(LedgerError, match="unavailable"): b.report([aa["id"]],JAN,END)
        rejected(c,"""INSERT INTO ledger.ledger_source(id,owner_id,account_id,source_key,format,parser_version,period_start,period_end)
          VALUES(:id,:owner,:account,'bad','synthetic','1','2026-01-01','2026-01-31')""",dict(id=uuid4(),owner=a.owner,account=ba["id"]))
        rejected(c,"""INSERT INTO ledger.canonical_transaction(id,owner_id,account_id,source_row_id,amount,direction,currency,posted_date)
          VALUES(:id,:owner,:account,:source,1,'debit','INR','2026-01-01')""",dict(id=uuid4(),owner=a.owner,account=aa["id"],source=bt["source_row_id"]))
        rejected(c,"""INSERT INTO ledger.transaction_link(id,owner_id,from_transaction_id,to_transaction_id,kind,actor_owner_id,reason)
          VALUES(:id,:owner,:f,:t,'transfer',:owner,'test')""",dict(id=uuid4(),owner=a.owner,f=at["id"],t=bt["id"]))
        # Verify the FK itself, not just a semantic trigger: a valid scope parent is missing.
        foreign_keys=c.execute(text("""SELECT pg_get_constraintdef(oid) FROM pg_constraint WHERE
            connamespace='ledger'::regnamespace AND contype='f'""")).scalars().all()
        assert any("owner_id, account_id, source_row_id" in fk for fk in foreign_keys)


def test_source_and_history_immutable_under_writer_role(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); tx=transaction(r,a)
        r.correct(tx["id"],0,"consumption")
        c.execute(text("SET LOCAL ROLE ledger_test_writer"))
        for table in ("source_row","ledger_source","canonical_transaction","classification_event","financial_account"):
            rejected(c,f"DELETE FROM ledger.{table} WHERE owner_id=:owner",dict(owner=r.owner))
            rejected(c,f"UPDATE ledger.{table} SET owner_id=owner_id WHERE owner_id=:owner",dict(owner=r.owner))
            rejected(c,f"TRUNCATE ledger.{table} CASCADE")
        assert r.transaction(tx["id"])["amount"] == D("10")


def test_restricted_writer_can_append_and_revoke_but_not_rewrite(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); p=transaction(r,a,"10",category="consumption")
        f=transaction(r,a,"2","credit","refund")
        c.execute(text("SET LOCAL ROLE ledger_test_writer"))
        link=r.link(p["id"],f["id"],"refund")
        r.revoke(link["id"])
        revoked=r._get("transaction_link",link["id"])
        assert revoked["revocation_actor_owner_id"]==r.owner and revoked["revoked_at"] is not None
        rejected(c,"UPDATE ledger.transaction_link SET revoked_at=NULL WHERE id=:id",dict(id=link["id"]))
        rejected(c,"DELETE FROM ledger.transaction_link WHERE id=:id",dict(id=link["id"]))
        r.correct(f["id"],1,"income",review_status="needs_review")
        totals=r.report([a["id"]],JAN,END)["totals"]
        assert totals["income"]==D("0") and totals["unknown_credits"]==D("2")


def test_correction_undo_and_direct_stale_event(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); tx=transaction(r,a)
        assert r.history(tx["id"])[0]["category"] == "unknown"
        first=r.correct(tx["id"],0,"consumption",reason="Fictional review")
        r.correct(tx["id"],1,"investment")
        undone=r.undo(tx["id"],2)
        assert undone["category"] == "consumption" and undone["undo_of_event_id"] is not None
        assert [e["revision"] for e in r.history(tx["id"])] == [0,1,2,3]
        with pytest.raises(LedgerError): r.correct(tx["id"],1,"investment")
        rejected(c,"""INSERT INTO ledger.classification_event(id,owner_id,transaction_id,revision,category,review_status,actor_kind,actor_owner_id,previous_event_id)
            VALUES(:id,:owner,:tx,2,'consumption','confirmed','synthetic_owner',:owner,:previous)""",
            dict(id=uuid4(),owner=r.owner,tx=tx["id"],previous=first["id"]))
        assert r.transaction(tx["id"])["amount"] == D("10")


@pytest.mark.parametrize("kind,direction,category",[("bank","debit","income"),("credit_card","credit","income"),
    ("bank","credit","consumption"),("bank","credit","investment"),("credit_card","debit","internal_transfer"),
    ("bank","credit","card_repayment"),("credit_card","debit","card_repayment"),("bank","debit","refund")])
def test_classification_compatibility(ledger_engine,kind,direction,category):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account(kind); tx=transaction(r,a,direction=direction)
        with pytest.raises(IntegrityError):
            with c.begin_nested(): r.correct(tx["id"],0,category)


def test_invalid_directions_currency_and_dates(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); s=r.source(a["id"],"s",JAN,END)
        row=r.source_row(s["id"],"1","1","debit","raw")
        for direction,currency,posted in [("invalid","INR","2026-01-01"),("debit","USD","2026-01-01"),("debit","INR","infinity")]:
            rejected(c,"""INSERT INTO ledger.canonical_transaction(id,owner_id,account_id,source_row_id,amount,direction,currency,posted_date)
              VALUES(:id,:owner,:account,:source,1,:direction,:currency,CAST(:posted AS date))""",
              dict(id=uuid4(),owner=r.owner,account=a["id"],source=row["id"],direction=direction,currency=currency,posted=posted))


def test_full_financial_fixture_and_partial_coverage(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); bank=r.account("bank"); second=r.account("bank"); card=r.account("credit_card")
        transaction(r,bank,"1000.10","credit","income")
        purchase=transaction(r,bank,"100.05",category="consumption")
        debit=transaction(r,bank,"200.00",category="internal_transfer")
        credit=transaction(r,second,"200.00","credit","internal_transfer")
        r.link(debit["id"],credit["id"],"transfer")
        transaction(r,card,"50.25",category="consumption")
        pay=transaction(r,bank,"50.25",category="card_repayment")
        settlement=transaction(r,card,"50.25","credit","card_repayment")
        r.link(pay["id"],settlement["id"],"repayment")
        transaction(r,bank,"100.00",category="investment")
        refund=transaction(r,bank,"20.00","credit","refund")
        r.link(purchase["id"],refund["id"],"refund")
        unknown=transaction(r,bank,"3.60","credit")
        ids=[bank["id"],second["id"],card["id"]]
        for account in ids: r.coverage(account,JAN,END,"complete","passed")
        report=r.report(ids,JAN,END); t=report["totals"]
        assert [t[k] for k in ("income","gross_consumption","refunds","net_consumption","investments","observed_cash_movement","unknown_credits")] == list(map(D,["1000.10","150.30","20.00","130.30","100.00","773.40","3.60"]))
        assert t["observed_income_less_net_consumption"] is None
        r.correct(unknown["id"],0,"income")
        assert r.report(ids,JAN,END)["totals"]["observed_income_less_net_consumption"] == D("873.40")
        partial=r.report([bank["id"]],JAN,END)
        assert "missing_accounts" in partial["warnings"] and partial["totals"]["observed_income_less_net_consumption"] is None
        r.coverage(bank["id"],JAN,END,"partial","unavailable",["missing_pages"])
        assert "incomplete_coverage" in r.report(ids,JAN,END)["warnings"]
        assert "no_data" in r.report([],JAN,END)["warnings"]


def test_coverage_conflicts_and_unposted_sources(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); transaction(r,a,"100","credit","income")
        r.coverage(a["id"],JAN,END,"complete","passed")
        assert r.report([a["id"]],JAN,END)["totals"]["observed_income_less_net_consumption"] == D("100")
        r.coverage(a["id"],date(2026,1,3),date(2026,1,4),"partial","failed")
        assert r.report([a["id"]],JAN,END)["totals"]["observed_income_less_net_consumption"] is None
        s=r.source(a["id"],"missing-normalization",JAN,END)
        r.source_row(s["id"],"1","unparsed","unknown","unknown")
        assert "unresolved_source_rows" in r.report([a["id"]],JAN,END)["warnings"]


def test_partial_cross_period_refunds_and_link_revocation(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); purchase=transaction(r,a,"100",category="consumption")
        f1=transaction(r,a,"30","credit","refund",FEB); f2=transaction(r,a,"70","credit","refund",FEB)
        r.link(purchase["id"],f1["id"],"refund"); second=r.link(purchase["id"],f2["id"],"refund")
        assert r.report([a["id"]],JAN,END)["totals"]["net_consumption"] == D("100")
        feb=r.report([a["id"]],FEB,date(2026,2,28))
        assert feb["totals"]["net_consumption"] == D("-100") and "cross_period_relationship" in feb["warnings"]
        extra=transaction(r,a,"0.01","credit","refund",FEB)
        with pytest.raises(IntegrityError):
            with c.begin_nested(): r.link(purchase["id"],extra["id"],"refund")
        with pytest.raises(IntegrityError):
            with c.begin_nested(): r.link(purchase["id"],f1["id"],"refund")
        r.correct(f2["id"],1,"income")
        assert r._get("transaction_link",second["id"])["revoked_at"] is not None
        r.undo(f2["id"],2)  # undo never silently restores the revoked link
        assert "unmatched_activity" in r.report([a["id"]],FEB,date(2026,2,28))["warnings"]
        r.link(purchase["id"],f2["id"],"refund")


def test_unmatched_pairs_and_reversal(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); b=r.account("bank")
        f=transaction(r,a,"10",category="internal_transfer"); t=transaction(r,b,"11","credit","internal_transfer")
        with pytest.raises(IntegrityError):
            with c.begin_nested(): r.link(f["id"],t["id"],"transfer")
        assert "unmatched_activity" in r.report([a["id"],b["id"]],JAN,END)["warnings"]
        p=transaction(r,a,"12",category="consumption"); rev=transaction(r,a,"12","credit","reversal")
        r.link(p["id"],rev["id"],"reversal")
        assert r.report([a["id"],b["id"]],JAN,END)["totals"]["net_consumption"] == D("0")


def run_race(engine, owner_id, actions):
    barrier=Barrier(2)
    def worker(action):
        try:
            with engine.begin() as c:
                r=Ledger(c,SyntheticOwner(owner_id)); barrier.wait(timeout=5); action(r)
            return "committed"
        except (LedgerError, IntegrityError):
            return "rejected"
    with ThreadPoolExecutor(max_workers=2) as pool:
        return sorted(pool.map(worker,actions))


def test_stale_concurrent_corrections(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); tx=transaction(r,a)
        oid=r.owner; tid=tx["id"]
    result=run_race(ledger_engine,oid,[lambda r:r.correct(tid,0,"consumption"),lambda r:r.correct(tid,0,"investment")])
    assert result==["committed","rejected"]
    with ledger_engine.begin() as c:
        assert len(Ledger(c,SyntheticOwner(oid)).history(tid))==2


def test_concurrent_refund_overallocation_direct_sql(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); p=transaction(r,a,"100",category="consumption")
        f1=transaction(r,a,"60","credit","refund"); f2=transaction(r,a,"60","credit","refund"); oid=r.owner
    def direct(refund):
        def action(repo):
            repo.connection.execute(text("""INSERT INTO ledger.transaction_link(id,owner_id,from_transaction_id,to_transaction_id,kind,actor_owner_id,reason)
              VALUES(:id,:owner,:f,:t,'refund',:owner,'synthetic_concurrency')"""),dict(id=uuid4(),owner=oid,f=p["id"],t=refund["id"]))
        return action
    assert run_race(ledger_engine,oid,[direct(f1),direct(f2)])==["committed","rejected"]
    with ledger_engine.begin() as c:
        assert c.scalar(text("SELECT count(*) FROM ledger.transaction_link WHERE owner_id=:o AND revoked_at IS NULL"),dict(o=oid))==1


def test_link_racing_correction_has_no_incompatible_active_link(ledger_engine):
    with ledger_engine.begin() as c:
        r=owner(c); a=r.account("bank"); p=transaction(r,a,"100",category="consumption")
        f=transaction(r,a,"20","credit","refund"); oid=r.owner
    results=run_race(ledger_engine,oid,[lambda r:r.link(p["id"],f["id"],"refund"),
                                      lambda r:r.correct(p["id"],1,"investment")])
    assert "committed" in results
    with ledger_engine.begin() as c:
        assert c.scalar(text("SELECT count(*) FROM ledger.transaction_link WHERE owner_id=:o AND revoked_at IS NULL"),dict(o=oid))==0
        r=Ledger(c,SyntheticOwner(oid))
        assert r.history(p["id"])[-1]["category"]=="investment"

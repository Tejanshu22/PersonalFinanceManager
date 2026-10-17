import os
from pathlib import Path

import pytest
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine, text
from sqlalchemy.engine import make_url


def pytest_addoption(parser):
    parser.addoption("--ledger-postgres", action="store_true", help="Require isolated PostgreSQL ledger tests")


def validate_test_url(raw, acknowledgement):
    try:
        url = make_url(raw)
        safe = (url.drivername == "postgresql+psycopg" and url.database == "finnest_ledger_test"
                and url.username == "ledger_test_owner" and url.host in ("ledger-test-db", "127.0.0.1", "localhost")
                and not url.query and acknowledgement == "DISPOSABLE_SYNTHETIC_DAY007")
    except Exception:
        safe = False
    if not safe:
        raise ValueError("Refusing non-disposable ledger test database")
    return url


@pytest.fixture(scope="session")
def ledger_engine(request):
    if not request.config.getoption("--ledger-postgres"):
        pytest.skip("PostgreSQL ledger tests NOT RUN; use --ledger-postgres and disposable test DB")
    raw = os.environ.get("TEST_DATABASE_URL", "")
    try:
        validate_test_url(raw, os.environ.get("LEDGER_TEST_DATABASE_ACK"))
    except ValueError:
        pytest.fail("Refusing non-disposable ledger test database", pytrace=False)
    engine = create_engine(raw, hide_parameters=True, connect_args={"options":"-c statement_timeout=15000 -c lock_timeout=10000"})
    with engine.connect() as conn:
        marker = conn.scalar(text("SELECT shobj_description(oid,'pg_database') FROM pg_database WHERE datname=current_database()"))
        if marker != "DISPOSABLE_SYNTHETIC_DAY007":
            pytest.fail("Disposable database marker absent", pytrace=False)
        # Require a fresh database. Tests never reset, truncate, drop or downgrade it.
        if conn.scalar(text("SELECT EXISTS(SELECT 1 FROM pg_namespace WHERE nspname='ledger')")):
            pytest.fail("Use a NEW disposable test database; existing ledger will not be reset", pytrace=False)
    previous = os.environ.get("DATABASE_URL")
    os.environ["DATABASE_URL"] = raw
    try:
        config = Config(str(Path(__file__).parents[1] / "alembic.ini"))
        command.upgrade(config, "head")
        command.upgrade(config, "head")  # repeated upgrade must be a no-op
    finally:
        if previous is None:
            os.environ.pop("DATABASE_URL", None)
        else:
            os.environ["DATABASE_URL"] = previous
    with engine.begin() as conn:
        conn.execute(text("GRANT USAGE ON SCHEMA ledger TO ledger_test_writer"))
        conn.execute(text("GRANT SELECT,INSERT,UPDATE,DELETE ON ALL TABLES IN SCHEMA ledger TO ledger_test_writer"))
    yield engine
    engine.dispose()

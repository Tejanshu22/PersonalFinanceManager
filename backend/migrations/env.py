"""Credentials are environment-only; SQL parameters and URLs are never logged."""
import os
from alembic import context
from sqlalchemy import create_engine

url = os.environ.get("DATABASE_URL")
if not url:
    raise RuntimeError("DATABASE_URL required for migration")
if url.startswith("postgresql://"):
    url = url.replace("postgresql://", "postgresql+psycopg://", 1)
engine = create_engine(url, hide_parameters=True)
with engine.connect() as connection:
    context.configure(connection=connection, transactional_ddl=True)
    with context.begin_transaction():
        context.run_migrations()
engine.dispose()

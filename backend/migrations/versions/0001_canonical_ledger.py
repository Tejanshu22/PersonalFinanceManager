"""Owner-scoped exact ledger; synthetic-development O-04 approval."""
from pathlib import Path
from alembic import op
from sqlalchemy import text

revision = "0001_canonical_ledger"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Version-owned SQL is immutable after acceptance; later changes get a new revision.
    sql = Path(__file__).with_suffix(".sql").read_text(encoding="utf-8")
    op.get_bind().execute(text(sql))


def downgrade():
    # No destructive automated recovery path, including on an accidentally selected DB.
    raise RuntimeError("Ledger history cannot be downgraded; use reviewed forward repair")

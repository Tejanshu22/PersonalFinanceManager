import pytest
from tests.conftest import validate_test_url

SAFE = "postgresql+psycopg://ledger_test_owner:synthetic@ledger-test-db/finnest_ledger_test"
ACK = "DISPOSABLE_SYNTHETIC_DAY007"


def test_disposable_target_allowed():
    assert validate_test_url(SAFE, ACK).database == "finnest_ledger_test"


@pytest.mark.parametrize("url,ack", [
    (SAFE, None), ("", ACK),
    (SAFE.replace("finnest_ledger_test", "finance_synthetic"), ACK),
    (SAFE.replace("ledger-test-db", "production.example"), ACK),
    (SAFE.replace("ledger_test_owner", "local_app"), ACK),
    (SAFE + "?host=production.example", ACK),
    ("sqlite://", ACK),
])
def test_unsafe_database_refused(url, ack):
    with pytest.raises(ValueError, match="Refusing non-disposable"):
        validate_test_url(url, ack)

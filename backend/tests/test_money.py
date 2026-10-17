from decimal import Decimal, localcontext, Rounded
import pytest
from app.ledger.money import money


@pytest.mark.parametrize("value", ["0.01", "0.10", "1.2300", "999999999999999999.99", Decimal("12.34")])
def test_money_exact(value):
    result = money(value)
    assert result == Decimal(value)
    assert result.as_tuple().exponent == -2


@pytest.mark.parametrize("value", [0.1, 1, True, None, "0", "-1", "1.005", "1000000000000000000",
                                     "NaN", "Infinity", "-Infinity", "not money", "1e-100", "1"*81])
def test_invalid_money(value):
    with pytest.raises(ValueError, match="invalid_money"):
        money(value)


def test_currency():
    with pytest.raises(ValueError):
        money("1.00", "USD")


def test_money_ignores_ambient_decimal_context():
    with localcontext() as context:
        context.prec = 2
        context.traps[Rounded] = True
        assert money("999999999999999999.9900") == Decimal("999999999999999999.99")

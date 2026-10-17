"""Approved O-04 exact input boundary. No rounding of financial facts."""
from decimal import Context, Decimal, InvalidOperation, localcontext, Inexact

LIMIT = Decimal("1000000000000000000")
PAISE = Decimal("0.01")


def money(value: str | Decimal, currency: str = "INR") -> Decimal:
    if currency != "INR" or not isinstance(value, (str, Decimal)):
        raise ValueError("invalid_money")
    if len(str(value)) > 80:
        raise ValueError("invalid_money")
    try:
        with localcontext(Context(prec=80)) as ctx:
            ctx.traps[Inexact] = True
            amount = Decimal(value)
            if not amount.is_finite() or not 0 < amount < LIMIT:
                raise ValueError("invalid_money")
            return amount.quantize(PAISE)
    except (InvalidOperation, Inexact):
        raise ValueError("invalid_money") from None

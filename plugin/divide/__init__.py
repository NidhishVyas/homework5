"""Division operation."""

from decimal import Decimal


def divide(a: Decimal, b: Decimal) -> Decimal:
    """Perform division of two Decimal numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

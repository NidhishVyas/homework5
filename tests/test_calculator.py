import pytest
from decimal import Decimal
from calculator import Calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal("2"), Decimal("2"), 'add', Decimal("4")),
    (Decimal("2"), Decimal("2"), 'subtract', Decimal("0")),
    (Decimal("2"), Decimal("2"), 'divide', Decimal("1")),
    (Decimal("2"), Decimal("2"), 'multiply', Decimal("4")),
])
def test_operation(a, b, operation, expected):
    result = Calculator.load_operation(operation)(a, b)
    assert result == expected, f"{operation} operation failed"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.load_operation("divide")(Decimal("10"), Decimal("0"))

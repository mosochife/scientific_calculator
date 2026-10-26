import pytest
from calculator import evaluate, CalculatorError


@pytest.mark.parametrize("expr, expected", [
    ("2+3*4", 14),
    ("(2+3)*4", 20),
    ("-2^2", -4),
    ("2^3^2", 512),
    ("10/4", 2.5),
    ("2*-3", -6),
    ("1.5+1.5", 3),
])
def test_valid_expressions(expr, expected):
    assert evaluate(expr) == pytest.approx(expected)


@pytest.mark.parametrize("expr", ["1/0", "(2+3", "2 3", "2+", "", "2 $ 3", "2+)"])
def test_errors_raise_calculator_error(expr):
    with pytest.raises(CalculatorError):
        evaluate(expr)

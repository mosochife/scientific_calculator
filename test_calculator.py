import pytest
from calculator import evaluate, calculate, CalculatorError


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


def test_calculate_alias():
    assert calculate("2+3*4") == pytest.approx(14)
    assert calculate("sin(30)", angle_mode="deg") == pytest.approx(0.5)


@pytest.mark.parametrize("expr, mode, expected", [
    ("sin(30)", "deg", 0.5),
    ("cos(60)", "deg", 0.5),
    ("tan(45)", "deg", 1),
    ("sin(pi/2)", "rad", 1),
    ("asin(0.5)", "deg", 30),
    ("sqrt(16)", "deg", 4),
    ("abs(-5)", "deg", 5),
    ("log(100)", "deg", 2),
    ("ln(e)", "deg", 1),
    ("2*pi", "rad", 2 * 3.141592653589793),
    ("sqrt(9)+sin(30)*2", "deg", 4),
])
def test_scientific_functions(expr, mode, expected):
    assert evaluate(expr, mode) == pytest.approx(expected)


@pytest.mark.parametrize("expr", [
    "foo(2)", "sin()", "sin(30", "sqrt",
])
def test_invalid_functions(expr):
    with pytest.raises(CalculatorError):
        evaluate(expr)


def test_invalid_angle_mode():
    with pytest.raises(CalculatorError):
        evaluate("sin(30)", "grad")


@pytest.mark.parametrize("expr, expected", [
    ("5!", 120),
    ("0!", 1),
    ("(2+1)!", 6),
    ("3!+1", 7),
    ("2*3!", 12),
])
def test_factorial(expr, expected):
    assert evaluate(expr) == pytest.approx(expected)


@pytest.mark.parametrize("expr", [
    "(-3)!", "2.5!", "171!", "sqrt(-1)",
    "log(0)", "ln(-5)", "tan(90)",
])
def test_domain_errors(expr):
    with pytest.raises(CalculatorError):
        evaluate(expr)

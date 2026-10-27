
import subprocess
import sys


def run_calculator(commands):
    return subprocess.run(
        [sys.executable, "main.py"],
        input="\n".join(commands) + "\n",
        text=True,
        capture_output=True,
        check=False,
    )


def test_help_command():
    result = run_calculator(["help", "quit"])

    assert "Available commands:" in result.stdout
    assert "history - show calculation history" in result.stdout


def test_history_shows_calculation():
    result = run_calculator(["2+3", "history", "quit"])

    assert "Result: 5" in result.stdout
    assert "2+3 = 5" in result.stdout



def test_clear_removes_calculation_history():
    result = run_calculator(
        ["2+3", "clear", "history", "quit"]
    )

    assert "Calculation history cleared." in result.stdout
    assert "No calculations yet." in result.stdout


def test_invalid_calculation_is_not_saved_in_history():
    result = run_calculator(["1/0", "history", "quit"])

    assert "Error: Division by zero" in result.stdout
    assert "No calculations yet." in result.stdout


def test_angle_mode_switching():
    result = run_calculator(["rad", "sin(pi/2)", "deg", "sin(30)", "quit"])

    assert "Angle mode set to rad." in result.stdout
    assert "Result: 1" in result.stdout
    assert "Angle mode set to deg." in result.stdout
    assert "Result: 0.5" in result.stdout

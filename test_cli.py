
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

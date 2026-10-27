# Scientific Calculator

A command-line scientific calculator built with Python. It evaluates mathematical expressions and supports scientific functions, angle modes, and calculation history.

## Features

- Basic arithmetic: addition, subtraction, multiplication, and division
- Scientific functions: sine, cosine, tangent, and inverse trigonometric functions
- Logarithms: `log()` and `ln()`
- Other functions: `sqrt()`, `abs()`, and factorial
- Mathematical constants: `pi` and `e`
- Degree and radian angle modes
- Calculation history
- Clear history with the `clear` command
- Built-in help with the `help` command
- Input validation and error handling

## Requirements

- Python 3
- No external packages are required for the calculator and its tests.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mosochife/scientific_calculator.git
cd scientific_calculator
```

### 2. Create and activate a virtual environment (optional)

On Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Run the calculator

```bash
python main.py
```

Enter a mathematical expression when prompted.

## Commands

| Command | Description |
|---|---|
| `help` | Display available commands |
| `history` | Show successful calculations |
| `clear` | Clear the current session's history |
| `deg` | Switch to degree mode |
| `rad` | Switch to radian mode |
| `quit` | Exit the calculator |

## Examples

```text
> 2 + 3
Result: 5

> sqrt(25)
Result: 5

> sin(30)
Result: 0.5

> rad
Angle mode set to rad.

> sin(pi/2)
Result: 1
```

Trigonometric functions use degree mode by default. Use `rad` to switch to radians.

## Running the Tests

Run the automated tests with:

```bash
python -m pytest -v
```

The tests cover calculator functionality and command-line behavior.

## Project Files

```text
scientific_calculator/
├── calculator.py       # Mathematical calculation engine
├── main.py             # Interactive command-line interface
├── test_calculator.py  # Calculator tests
├── test_cli.py         # Command-line interface tests
└── README.md           # Project documentation
```

## Future Improvements

- Add more scientific functions
- Improve result formatting and rounding options
- Add more automated tests

## Author

**mosochife**

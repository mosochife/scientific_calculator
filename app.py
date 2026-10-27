import math

from flask import Flask, jsonify, render_template, request

from calculator import evaluate, CalculatorError

app = Flask(__name__)

MAX_LENGTH = 200  # reject huge inputs before they reach the parser


def format_result(value):
    """Round away floating-point noise and show whole numbers without '.0'."""
    if not math.isfinite(value):
        raise CalculatorError("Result is too large")
    value = round(value, 10)
    if value == int(value) and abs(value) < 1e15:
        return int(value)
    return value


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        data = {}
    expression = data.get("expression", "")
    angle_mode = data.get("angle_mode", "deg")

    if not isinstance(expression, str):
        return jsonify(error="Expression must be text"), 400
    if len(expression) > MAX_LENGTH:
        return jsonify(error=f"Expression too long (max {MAX_LENGTH} characters)"), 400

    try:
        result = evaluate(expression, angle_mode)
        return jsonify(result=format_result(result))
    except CalculatorError as err:
        return jsonify(error=str(err)), 400
    except OverflowError:
        return jsonify(error="Result is too large"), 400
    except RecursionError:
        return jsonify(error="Expression is too complex"), 400


if __name__ == "__main__":
    app.run(debug=True)  # debug=True is for local development only

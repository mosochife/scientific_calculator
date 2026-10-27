from calculator import evaluate, CalculatorError


def main():
    print("Scientific Calculator")
    print("Type an expression such as 2+3*4 or sin(30).")
    print("Use 'deg' or 'rad' to change angle mode.")
    print("Type 'quit' to exit.")

    angle_mode = "deg"

    while True:
        expression = input(f"[{angle_mode}] Enter expression: ").strip()

        if expression.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        if expression.lower() in ("deg", "rad"):
            angle_mode = expression.lower()
            print(f"Angle mode set to {angle_mode}.")
            continue

        try:
            result = evaluate(expression, angle_mode)
            print(f"Result: {result}")
        except CalculatorError as error:
            print(f"Error: {error}")
        except (ValueError, OverflowError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()

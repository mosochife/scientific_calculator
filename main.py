
from calculator import evaluate, CalculatorError


def main():
    print("Scientific Calculator")
    print("Type an expression such as 2+3*4 or sin(30).")
    print("Use 'deg' or 'rad' to change angle mode.")
    print("Type 'history' to see previous calculations.")
    print("Type 'quit' to exit.")

    angle_mode = "deg"
    history = []

    while True:
        expression = input(f"[{angle_mode}] Enter expression: ").strip()

        if expression.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        if expression.lower() in ("deg", "rad"):
            angle_mode = expression.lower()
            print(f"Angle mode set to {angle_mode}.")
            continue
         
        if expression.lower() == "clear":
            history.clear()
            print("Calculation history cleared.")
            continue

        if expression.lower() == "history":
            if not history:
                print("No calculations yet.")
            else:
                print("Calculation history:")
                for item in history:
                    print(item)
            continue

        try:
            result = evaluate(expression, angle_mode)
            formatted_result = f"{result:.10g}"
            print(f"Result: {formatted_result}")
            history.append(f"{expression} = {formatted_result}")
        except CalculatorError as error:
            print(f"Error: {error}")
        except (ValueError, OverflowError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()

        

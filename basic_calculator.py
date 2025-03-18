def basic_calculator():
    """
A simple calculator program that takes two numbers and an operator as input and returns the result of the operation. 
    """
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operator == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operator == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operator == "/":
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operator. Please enter one of the following: +, -, *, /")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    basic_calculator()
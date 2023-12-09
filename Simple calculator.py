def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculator():
    print("Simple Calculator\n")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = int(input("Enter the operation number (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == 1:
        result = add(num1, num2)
        operation = "Addition"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "Division"
    else:
        print("Invalid operation choice. Please enter a number between 1 and 4.")
        return

    print(f"\n{operation} Result: {result}")

if __name__ == "__main__":
    calculator()

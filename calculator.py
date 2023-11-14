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
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation : ")

    # Perform calculation based on user's choice
    if operation == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please enter a valid operation.")

# call the "calculator" function

calculator()

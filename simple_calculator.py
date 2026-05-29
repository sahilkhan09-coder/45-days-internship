def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Operations: add, subtract, multiply, divide")
choice = input("Enter operation: ").lower()

if choice in operations:
    result = operations[choice](num1, num2)
    print("Result:", result)
else:
    print("Invalid operation")

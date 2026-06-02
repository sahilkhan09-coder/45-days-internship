from typing import Optional


def add(a: float, b: float) -> float:
    """
    Adds two numbers and returns the result.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtracts second number from first number and returns the result.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the result.
    """
    return a * b


def divide(a: float, b: float) -> Optional[float]:
    """
    Divides first number by second number.
    Returns None if division by zero is attempted.
    """
    if b == 0:
        return None
    return a / b


def power(base: float, exp: float) -> float:
    """
    Raises base to the power of exp and returns the result.
    """
    return base ** exp


def modulo(a: int, b: int) -> int:
    """
    Returns the remainder when a is divided by b.
    Returns 0 if division by zero is attempted.
    """
    if b == 0:
        print("Error: Modulo by zero is not allowed.")
        return 0
    return a % b


print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 0))
print("Power:", power(2, 3))
print("Modulo:", modulo(10, 3))

"""
Simple Calculator Application
Course: Learning Manual Testing (OUSL)
Version: 2.0.0 (Upgraded & Bug-Fixed Version)
Author: numair-it
GitHub: https://github.com/numair-it/simple-calculator
"""

import math

__version__ = "2.0.0"

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts b from a."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """
    Divides a by b.
    Fixed in v2.0.0 (BUG-001 / TC_CALC_012):
    Handles division by zero safely without crashing.
    """
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    """
    Calculates modulus (remainder of a / b).
    Fixed in v2.0.0 (BUG-002 / TC_CALC_014):
    Handles modulus by zero safely without crashing.
    """
    if b == 0:
        return "Error: Modulo by zero is not allowed."
    return a % b

def power(a, b):
    """Calculates a raised to power b."""
    try:
        return a ** b
    except OverflowError:
        return "Error: Result is too large (Overflow)."

def square_root(a):
    """
    Calculates square root of a.
    Fixed in v2.0.0 (BUG-003 / TC_CALC_018):
    Handles negative numbers safely without crashing.
    """
    if a < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.sqrt(a)

def get_valid_number(prompt):
    """
    Safely prompts user for numeric input with validation.
    Fixed in v2.0.0:
    - Resolves BUG-004 (TC_CALC_019): Non-numeric string input handling.
    - Resolves BUG-005 (TC_CALC_020): Empty / blank input handling.
    """
    while True:
        raw_input = input(prompt).strip()
        if not raw_input:
            print("Error: Input cannot be empty. Please enter a valid number.")
            continue
        try:
            return float(raw_input)
        except ValueError:
            print("Error: Invalid input! Please enter a valid numeric value.")

def display_menu():
    """Displays calculator menu options."""
    print("\n" + "=" * 45)
    print(f"   SIMPLE CALCULATOR (v{__version__}) - UPGRADED")
    print("=" * 45)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Square Root (sqrt)")
    print("8. Exit")
    print("-" * 45)

def run_calculator():
    """Main interactive loop for the calculator."""
    print(f"\nWelcome to Simple Calculator Application v{__version__}")
    print("All reported defects from v1.0.0 have been fixed.")
    
    while True:
        display_menu()
        choice = input("Enter choice (1-8): ").strip()
        
        if choice == '8':
            print("\nExiting Calculator. Thank you!")
            break
            
        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = get_valid_number("Enter first number: ")
            num2 = get_valid_number("Enter second number: ")
            
            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Result: {num1} / {num2} = {result}")
            elif choice == '5':
                result = modulus(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Result: {num1} % {num2} = {result}")
            elif choice == '6':
                result = power(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Result: {num1} ^ {num2} = {result}")
                
        elif choice == '7':
            num = get_valid_number("Enter number: ")
            result = square_root(num)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: sqrt({num}) = {result}")
        else:
            print("Error: Invalid choice! Please select an option between 1 and 8.")

if __name__ == "__main__":
    run_calculator()

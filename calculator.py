"""
Simple Calculator Application
Course: Learning Manual Testing (OUSL)
Version: 1.0.0 (Initial Application)
Author: numair-it
GitHub: https://github.com/numair-it/simple-calculator
"""

import math

__version__ = "1.0.0"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # In v1.0.0: No division by zero check (intentional defect for testing)
    return a / b

def modulus(a, b):
    # In v1.0.0: No modulo by zero check (intentional defect for testing)
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    # In v1.0.0: No negative number check (intentional defect for testing)
    return math.sqrt(a)

def display_menu():
    print("\n" + "=" * 40)
    print(f"   SIMPLE CALCULATOR (v{__version__})")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Square Root (sqrt)")
    print("8. Exit")
    print("-" * 40)

def run_calculator():
    print(f"Welcome to Simple Calculator Application v{__version__}")
    
    while True:
        display_menu()
        choice = input("Enter choice (1-8): ")
        
        if choice == '8':
            print("Exiting Calculator. Thank you!")
            break
            
        if choice in ('1', '2', '3', '4', '5', '6'):
            # In v1.0.0: Direct float conversion without validation (crashes on invalid/empty input)
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
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
                print(f"Result: {num1} / {num2} = {result}")
            elif choice == '5':
                result = modulus(num1, num2)
                print(f"Result: {num1} % {num2} = {result}")
            elif choice == '6':
                result = power(num1, num2)
                print(f"Result: {num1} ^ {num2} = {result}")
                
        elif choice == '7':
            # In v1.0.0: Direct float conversion without validation
            num = float(input("Enter number: "))
            result = square_root(num)
            print(f"Result: sqrt({num}) = {result}")
        else:
            print("Invalid choice! Please select an option between 1 and 8.")

if __name__ == "__main__":
    run_calculator()

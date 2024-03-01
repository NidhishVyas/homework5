import os
import importlib
from decimal import Decimal


def discover_operations():
    plugins_dir = "plugin"

    operations = []

    for item in os.listdir(plugins_dir):
        item_path = os.path.join(plugins_dir, item)

        if os.path.isdir(item_path):
            operations.append(item)

    return operations


def display_menu(operations):
    print("\nAvailable operations:")
    for operation in operations:
        print(operation)
    print("exit")


def perform_operation(operation):
    try:
        operation_module = importlib.import_module(f"plugin.{operation}")
        operation_func = getattr(operation_module, operation)
        a = Decimal(input("Enter first number: "))
        b = Decimal(input("Enter second number: "))
        result = operation_func(a, b)
        print(f"Result of {operation}({a}, {b}) = {result}")
    except (ImportError, AttributeError):
        print(f"Error: Operation '{operation}' not found or invalid")
    except Exception as e:
        print(f"An error occurred: {e}")


def calculate_and_print(a, b, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        operation_module = importlib.import_module(f"plugin.{operation_name}")
        operation_func = getattr(operation_module, operation_name)
        result = operation_func(a_decimal, b_decimal)
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    operations = discover_operations()
    while True:
        display_menu(operations)
        choice = input("Enter the operation name (or 'exit' to quit): ")
        if choice.lower() == "exit":
            print("Exiting...")
            break
        elif choice in operations:
            perform_operation(choice)
        else:
            print("Invalid operation name. Please select a valid operation or 'exit'.")


if __name__ == "__main__":
    main()

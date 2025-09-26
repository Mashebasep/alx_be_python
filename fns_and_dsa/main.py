from arithmetic_operations import perform_operation
# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
# Perform operation
result = perform_operation(num1, num2, operation)
# Show result
print("Result:", result)

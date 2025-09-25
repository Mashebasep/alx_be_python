from arithmetic_oprations import perform_operation
# Ask user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()
# Perform the calculation
result = perform_operation(num1, num2, operation)
# Display the result
print(f"The result is: {result}")



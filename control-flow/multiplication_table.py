# prompt user for number
number = int(input("Enter a number to see its multiplication table: "))
# Generate and print multiplication table
for i in range(1, 11):
    product = number * 1
    print(f"{number} * {i} = {product}")

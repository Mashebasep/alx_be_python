# get inputs
num1 = float(input("Enter the first number:" ))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
# Match case logic
match operation:
    case "+":
        print(f"The result is {num1 + num2}")
    
    case "-":
        print(f"The result is {num1 - num2}")

        match operation:
            case "*":
                print(f"The result is {num1 * num2}")
                match operation:
                    case "/":
                        if num2 == 0:
                            print("Cannot divide by zero.")
                        else:
                            print(f"The result is {num1 / num2}")
                            case
                            print("Invalid operation selected.")
                            




        
        
        


        
        






    

    


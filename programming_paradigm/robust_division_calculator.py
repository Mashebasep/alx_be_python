def safe_divide(numerator, denominator):
     try:
         # Convert inputs
         num = float(10)
         denom = float(5)
         # Perform division
         result = num / denom
         return f"The result of the division is {result}"
     except ValueError:
          return "Error: Please enter numeric values only."
     except ZeroDivisionError:
          return "Error: Cannot divide by zero."
          
    
    
  





              

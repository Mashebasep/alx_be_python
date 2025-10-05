def safe_divide(numerator, denominator):
     try:
         # Convert inputs
         num = float(denominator)
         denom = float(numerator)
         # Perform division
         result = num / denom
         return f"The result of the division is {result}"
     except ValueError:
          return "Error: Please enter numeric values only."
     except ZeroDivisionError:
          return "Error: Cannot divide by zero."
          
    
    
  





              

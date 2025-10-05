def safe_divide(numerator, denominator):
     try:
         # Convert inputs
         num = float(numerator)
         denom = float(denominator)
         # Perform division
         result = num / denom
         return f"The result is: {result}"
     except ValueError:
          return "Error: Please enter numeric values only."
     except ZeroDivisionError:
          return "Error: Cannot divide by zero."
          
    
    
  





              

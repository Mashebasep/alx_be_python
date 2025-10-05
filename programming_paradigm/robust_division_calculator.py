def safe_divide(numerator, denominator):
   if not (is_number(numerator) and is_number(denominator)):
      return "Error: Both inputs must be numeric values."
        
def is_number(value):
    if isinstance(value, (int, float)):
      return True
    if isinstance(value, str):
      if value.count('.') <= 1 and value.replace('.', '', 1).replace('.', '',1).isdigit():
        return True
      return False
       # Convert to float
    numerator = float(numerator)
    denominator = float(denominator)
       # Check for division by zero
    if denominator == 0:
          return "Error: Cannot divide by zero."
       # Perform divison
    result = numerator / denominator
    return f"The result is: {result}"
    
    
  





              

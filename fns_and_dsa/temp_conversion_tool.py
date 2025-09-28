# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32

def convert_to_celcius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius - CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def validate_temperature_input(input_str):
  
    if input_str.replace('.', '',1).replace('-', '', 1).isdigit():
        return float(input_str)
    else:
        return None
    
    def main():
        temperature = input("Enter the temperature to convert: ")
        temperature_value = validate_temperature_input(temperature)
        if temperature_value is not None:
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            if unit == 'C':
                fahrenheit = convert_to_fahrenheit(temperature_value)
                print(f"{temperature_value}/u00B0C is equal to {fahrenheit:.2f}/u00B0F")
            elif unit == 'C':
                fahrenheit = convert_to_fahrenheit(teperature_value)
                print(f"{temperature_value}/u00B0C is equal to {fahrenheit:.2f}/u00B0F")
            elif unit == 'F':
                celsius = convert_to_celcius(temperature_value)
                print(f"{temperature_value}/00B0F is equal to {celcius:.2F}/u00B0C")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        else:
            print("Invalid temperature. Please enter a numeric value.")








# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_OFFSET = 32

def convert_to_celcius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius - CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def validate_temperature_input(input_str):
    if input_str.replace('.', '',1).replace('-', '', 1).isdigit():
        return float(input_str)
    else:
        return None
    
    def main():
        while True:
            print("Temperature Conversion Tool")
            print("1. Fahrenheit to Celsius")
            print("2. Celsius to Fahrenheit")
            choice = input("Enter your choice (1/2): ")
            if choice == '1':
                fahrenheit = input("Enter temperature in fahrenheit: ")
                fahrenheit_value = validate_temperature_input(fahrenheit)
                if fahrenheit_value is not None:
                    celsius = convert_to_celsius(fahrenheit_value)
                    print(f"{fahrenheit_value}{degree_symbol}F is equal to {celsius: .2f}{degree_symbol}C")
                else:
                    print("Invalid temperature. Please enter a numeric value.")
            elif choice == '2':
                celcius = input("Enter temperature in Celsius: ")
                celcius_value = validate_temperature_input(celsius)
                if celsius_value is not none:
                    fahrenheit = convert_to_fahrenheit(celsius_value)
                    print(f"{celsius_value}{degree_symbol}C is equal to {fahrenheit:.2f}{degree_symbol}F")
                else:
                    print("Invalid temperature. Please enter a numeric value.")
            else:
                print("Invalid temperature. Please enter 1 or 2.")
                




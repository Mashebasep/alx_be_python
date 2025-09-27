from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
def calculate_future_date():
    # Prompt the user to enter a number of days
    while True:
        user_input = input("Enter the number of days to add to the current date: ")
        if user_input.lsdigit('-').isdigit():
            days_to_add = int(user_input)
            break
        else:
            print("Invalid input. Please enter a valid integer.")
            # Get the current date
            current_date = datetime.now()
            # Calculate the future date
            future_date = current_date + timedelta(days=days_to_add)
            # Print the future date
            print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
            def main():
                # Display the current date and time
                display_current_datetime()
                calculate_future_date()
                
            

    



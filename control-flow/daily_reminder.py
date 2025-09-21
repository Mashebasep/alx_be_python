# Prompt for inputs
task = input("Enter your task:")
priority = input("Enter your priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()
# Process based on priority
match priority:
    case "high":
        remnider = f"Reminder: '{task}' is high priority."
    case "medium":
        reminder = f"Reminder: '{task}' is medium priority."
    case "low":
        reminder = f"Reminder: '{task}' is low priority."
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority"
        # Modify reminder if task is time-bound
        if time_bound == "yes":
            reminder += "that requires immediate attention today!"
            # Print reminder
            print(reminder)




        






        



                    







        


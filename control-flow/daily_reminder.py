# Ask user for task details
task = input("Enter your task: ")
priority = input("Enter the task's priority (high/medium/low):").strip().lower()
time_bound = input("Is it time-bound? (yes/no):").strip().lower()
# Match Case for priority + time-bound
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"High priority task '{task}' requires immediate attention today!"
        else:
            reminder = f"High priority task '{task}' should be done soon."
    case "medium":
        if time_bound == "yes":
            reminder = f"Medium priority task '{task}' requires immediate attention today!"
        else:
            reminder = f"Medium priority task '{task}' should be planned for near future."
    case "low":
        if time_bound == "yes":
            reminder = f"Low priority task '{task}' requires immediate attention today!"
        else:
            reminder = f"Low priority task '{task}' can be done when you have free time."
    case _:
        reminder = f"Task '{task}' has an UNKNOWN priority."
        # Print Customized Reminder
        print(reminder)
        
            


# Ask user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
# Match Case for priority + time-bound
match priority:
    case "high":
        priority_level = "high"
    case "medium":
        priority_level ="medium"
    case "low":
        priority_level ="low"
    case _:
        priority_level = "unknown"

        reminder = f"Reminder: '{task}' has ({priority_level}) priority."
        if time_bound == "yes"and priority == "high":
            reminder += " that requires immediate attention today!"
            print(reminder)
            





            


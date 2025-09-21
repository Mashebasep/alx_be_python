# Prompt user single task and details
task = input("Enter you task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
# Start building the reminder message
reminder = f"Reminder: '{task}' is"
# Match case for priority
match priority:
    case "high":
        reminder += "a high priority task"
    case "medium":
        reminder += "a medium priority task"
    case "low":
        reminder += "a low priority task"
    case _:
        reminder += f"a task with unknown priority ({priority})"
        # Add time-bound
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
            # Print message
            print(reminder)
            
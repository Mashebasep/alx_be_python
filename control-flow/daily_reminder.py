# Prompt for task details
task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()
# Process based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is HIGH priority"

        match priority:
            case "medium":
                reminder = f"Reminder: '{task}' is MEDIUM priority"

                match priority:
                    case "low":
                        reminder = f"Reminder: '{task}' is LOW priority"
                        reminder = f"Reminder: '{task}' has an unknown priority"
                        # Fix reminder if task is time-bound
                        if time_bound == "yes":
                            reminder += "that requires attention!"
                            print(remider)


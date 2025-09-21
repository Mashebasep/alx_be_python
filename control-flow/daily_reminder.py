# Prompt the user for a single task and details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        message = f"reminder: '{task}' is a high priority task"
        match priority:
            case "medium":
                message = f"Reminder: '{task}' is a medium priority task"
                match priority:
                    case "low":
                        message = f"Reminder: '{task}' is a low priority task"
                        match priority:
                            case "low":
                                message = f"Reminder: '{task}' has unknown priority level"
                                # Customized Reminder
                                reminder = f"Reminder: Your task '{task}' has {priority} priority."
                                if time_bound == "yes" and "high priority" in message:
                                    message += "that requires immediate attention today!"
                                    print(reminder)







        


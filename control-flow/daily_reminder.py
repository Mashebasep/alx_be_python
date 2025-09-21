# Prompt the user for a single task and details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        reminder = f"Reminder: Your task '{task}' has high priority."
        match priority:
            case "medium":
                reminder = f"Reminder: Your task '{task}' has medium priority."
                match priority:
                    case "low":
                        reminder = f"Reminder: Your task '{task}' has low priority."
                        case
                        reminder = f"Reminder: Your task '{task}' has an unknown priority."
                        if time_bound == "yes":
                            reminder += "This task requires immediate attention today!"
                            
                            reminder = f"Reminder: Your task '{task}' has an unknown priority."
                            # Customized Reminder
                            print(reminder)

                    







        


# User task details
task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Time Bound (yes/no): ").lower()
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
                        match priority:
                            case "low":
                                reminder = f"Reminder: '{task}' has an unknown priority"
                                # Modify reminder if task is time_bound
                        if time_bound == "yes":
                            reminder += "that requires immediate attention today!"

                            print(reminder)


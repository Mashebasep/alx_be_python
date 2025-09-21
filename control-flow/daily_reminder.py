# Prompt the user for a single task and details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time_bound? (yes/no): ").lower()
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has unknown priority"
        if time_bound == "yes" and "high priority" in message:
            message += "that requires immediate attention today!"
            print("reminder")
            





        






        



                    







        


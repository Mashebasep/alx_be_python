# Prompt for inputs
task = input("Enter the task: ")
priority = input("Enter the task priority (high,medium,low): ")
time_bound = input("Is the task time-bound? (yes/no): ")
# Match Case for priority
match priority:
    case "high":
        reminder = f"Reminder: {task} is a HIGH priority task"
    case "medium":
        reminder = f"Reminder: {task} is a MEDIUM priority task"
    case "low":
        reminder = f"Reminder: {task} is a LOW priority task"
    case _:
        reminder = f"Reminder: {task} has an unknown priority"
    # If the task is time-bound, append required phrase
        if time_bound.lower() == "yes":
            reminder += "that requires immediate attention today!"
            # print customized reminder
            print(reminder)
            


        






        



                    







        


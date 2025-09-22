# Ask user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
# Match Case for priority + time-bound
match priority:
    case "high":
        reminder_message = f"'{task}' is a **high** priority task"
    case "medium":
        reminder_message = f" '{task}' is a **medium** priority task"
    case "low":
        reminder_message = f"'{task}' is a **low** priority task. consider completing it when you have free time"
    case _:
        reminder_message = f"'{task}' is a task with an **Unspecified** priority"

        if time_bound == "yes" and priority in ["high", "medium"]:
            remider_message = f"{reminder_message} that requires immediate attention today!"
        elif time_bound == "yes" and priority == "low":
            reminder_message = f"'{task}' is a **low** priority task, but it requires attention today!"
        elif time_bound == "no" and priority in ["high","medium"]:
            reminder_message = f"(reminder_message)."

            print(f"/nReminder: {reminder_message}")
            




            


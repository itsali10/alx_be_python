task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time == "yes":
            print (f"'{task}' is a high priority task that requires immediate attention today!")
        elif time == "no":
            print(f"'{task}' is a high priority task. Consider completing it when you have free time.")
        else:
            print("Time-bound is either yes or no")
    case "medium":
        if time == "yes":
            print (f"'{task}' is a medium priority task that requires immediate attention today!")
        elif time == "no":
            print(f"'{task}' is a medium priority task. Consider completing it when you have free time.")
        else:
            print("Time-bound is either yes or no")
    case "low":
        if time == "yes":
            print (f"'{task}' is a low priority task that requires immediate attention today!")
        elif time == "no":
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("Time-bound is either yes or no")
    case _:
        print("Priority can only be high, medium or low")
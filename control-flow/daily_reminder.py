task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ") 
time_bound = input("Is it time-bound? (yes/no): ")  
reminder_message =f"Reminder: '{task}' is a {priority} priority task"
match priority:
    case "high":
      if time_bound == "yes":
          reminder_message += " that requires immediate attention today!"
      else:
        reminder_message += ". Consider completing it when you have free time."
    case "medium":
          if time_bound == "yes":
              reminder_message += " that should be addressed within the next few days."
          else:
              reminder_message += ". Try to get to it when possible."
    case "low":
          if time_bound == "yes":
              reminder_message += " that can be done sometime this week."
          else:
              reminder_message += ". No rush, do it whenever you feel like it."
    case _:
          reminder_message = "Error: Invalid priority level."
print(reminder_message)    
        
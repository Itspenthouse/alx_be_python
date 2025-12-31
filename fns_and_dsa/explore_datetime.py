import datetime
def display_current_datetime():
    datetime = datetime.datetime.now()    
    current_date = datetime.strptime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", current_date)
   
def calculate_future_date():
try:
  number_of_days = int(input("Enter number of days to add to current date: "))
  future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
  future_date = datetime.strptime("%Y-%m-%d %H:%M:%S", future_date)
  print("Future Date :", future_date)
except ValueError:
  print("Enter a valid number for a date")
  
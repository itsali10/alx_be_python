from datetime import *

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

def calculate_future_date(number_of_days):
    future_date = date.today()+timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(number_of_days)

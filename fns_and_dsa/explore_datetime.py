from datetime import *

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {date.today()+timedelta(days=number_of_days)}")

from datetime import *

print(f"Current date and time: {datetime.now()}")
number_of_days = int(input("Enter the number of days to add to the current date:"))
print(f"Future date: {date.today()+timedelta(days=number_of_days)}")
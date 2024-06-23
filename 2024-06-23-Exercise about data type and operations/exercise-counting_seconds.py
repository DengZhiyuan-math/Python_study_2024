# get the total number of minutes, hours and days from the user
# calculate the total number of seconds
# display the total number of seconds

from decimal import Decimal as decimal

num_seconds = None
num_minutes = decimal(input("Enter the number of minutes: "))
num_hours = decimal(input("Enter the number of hours: "))
num_days = decimal(input("Enter the number of days: "))

num_seconds = num_minutes * 60 + num_hours * 3600 + num_days * 86400

print("The total number of seconds is: ", num_seconds)

# 2024-06-23-Exercise about data type and operations/exercise-counting_seconds.py

# input the number of hours
hours = int(input("Enter Hours: "))

# input the number of days

days = int(input("Enter Days: "))

# input the number of minutes

minutes = int(input("Enter Minutes: "))

# calculate the numbers of seconds
seconds = minutes * 60 + hours * 60 * 60 + days * 24 * 60 * 60

# output the number of seconds

print("The number of seconds is "+ str(seconds))
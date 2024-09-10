# get unit_price and amount from the user
# float creates error in the results of the program, 47.6999999996 but not 47.7
# decimal is used to solve this problem
from decimal import Decimal as decimal
unit_price = decimal(input("Enter the unit price: "))
num_items = int(input("Enter the number of items: "))
# calculate the total price
total_price = unit_price * num_items

# display the total price
print("The total price is: ", total_price)

# get amount from the user
amount = decimal(input("Enter the amount paid: "))

# calculate the change
change = amount - total_price
# float and decimal can not be mixed together


# display the change
print("The change is: ", change)


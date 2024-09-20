# input the unit price of the product
unit_price = input("请输入商品的单价：")

# input the quantity of the product
quantity = input("请输入商品的数量：")

# input the amount of money
amount = input("请输入支付的金额：")

# convert the input data to the float type
unit_price = float(unit_price)
quantity = float(quantity)
amount = float(amount)

# calculate the change
change = amount - unit_price * quantity

# output the change
print("找零：" + str(change))


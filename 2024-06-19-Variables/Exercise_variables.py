var_1 = input("Please enter the first variables: ")
var_2 = input("Please enter the second variables: ")

print("The first variable is: ", var_1)
print("The second variable is: ", var_2)

# var_null = var_2
# var_2 = var_1
# var_1 = var_null
# Python 特有的
var_1, var_2 = var_2, var_1
print(var_1, var_2)

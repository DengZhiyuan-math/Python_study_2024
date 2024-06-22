"""
数据类型的转换
    运算符：
        算法运算符
        增强运算符
"""

# int float str 之间的转换

str_usd = input("请输入美元的金额：")
# 数据输入类型都是字符串

int_usd = int(str_usd)

result = int_usd * 6.9

print(result)

# 现在我们希望用字符串来输出结果

# 转换为str

# str + 数值 是没有意义的

result = str(result)

print("结果是" + result)



# 算数运算符
# + - * / % // **
# // 整除
# / 除法
# % 余数
# ** 幂运算

print(10 // 3)

print( 5 ** 2)  # 5的2次方

print(27 % 10) # 获取个位数

# 增强运算符
number01 = 10
print(number01+1)
print(number01)# 10 number01 没有发生变化


# or

number01 = 10
number01 += 1

# or

number01 = 10
number01 = number01 + 1

print(number01) # 11 number01 发生了变化

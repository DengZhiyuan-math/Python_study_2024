def input_integer():
    while True:
        integer = input("Please enter a four-digit integer: ")
        if integer.isdigit() and len(integer) == 4:
            return int(integer)  # Convert the input to an integer before returning
        else:
            print("The input must be a four-digit integer. Please try again.")
def summation_digits(integer):
        # 将整数转换为字符串，然后遍历每个字符
        return sum(int(digit) for digit in str(integer))


if __name__ == "__main__":
    sum = summation_digits(input_integer())
    print(f"the summation of every digits of the integer is: {sum}")


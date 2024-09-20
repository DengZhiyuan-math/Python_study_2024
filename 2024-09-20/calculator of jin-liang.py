'''
one jin is equal to 16 liang
'''

# input the number of jin and liang
# jin = int(input("please enter the number of jin:"))
# liang = int(input("please enter the number of liang:"))


# jin_liang = input("Please enter the number of jin first then the liang, separated by space: ").split()
# jin = int(jin_liang[0])
# liang = int(jin_liang[1])
#
# result = jin * 16 + liang
#
# print(f"in total, there is {result} liang")

def get_input():
    while True:
        jin_liang = input("Please enter the number of jin first then the liang, separated by space: ")
        try:
            jin_liang_list = jin_liang.split()
            if len(jin_liang_list) != 2:
                raise ValueError("Please enter exactly two numbers.")
            jin = int(jin_liang_list[0])
            liang = int(jin_liang_list[1])
            return jin, liang
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def calculate_total(jin, liang):
    result = jin * 16 + liang
    return result

def main():
    jin, liang = get_input()
    result = calculate_total(jin, liang)
    print(f"In total, there is {result} liang.")

if __name__ == "__main__":
    main()
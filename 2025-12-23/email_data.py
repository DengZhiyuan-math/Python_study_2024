# Use the file name mbox-short.txt as the file name
file_name = input("Enter file name: ")
fh = open(file_name)
summation = 0
number_of_lines = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    position_space = line.rfind(" ")
    number = float(line[position_space + 1:])
    number_of_lines = number_of_lines + 1
    summation = summation + number
print("Average spam confidence:", summation / number_of_lines)
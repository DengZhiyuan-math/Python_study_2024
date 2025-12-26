# import re
#
# fh = open('actual_data', 'r')
# all_numbers = []
# for line in fh:
#     all_numbers.extend(re.findall('[0-9]+', line))
# total = sum(int(i) for i in all_numbers)
# print(total)
import re
import re
print(sum(int(n) for n in re.findall('[0-9]+', open('actual_data').read())))



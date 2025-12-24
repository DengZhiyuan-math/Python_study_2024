file_name = input("Enter file name: ")
fh = open(file_name)
list_words = list()
for line in fh:
    words = line.split()
    for word in words:
        if word in list_words:
            continue
        else:
            list_words.append(word)
list_words.sort()
print(list_words)

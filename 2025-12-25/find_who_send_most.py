file_name = "mbox-short"
sender_count = dict()
emails = open(file_name)
for line in emails:
    line = line.strip()
    if not line.startswith("From "):
        continue
    else:
        words = line.split( )
        sender_count[words[1]]= sender_count.get(words[1],0) + 1
most_sent = max(sender_count, key=sender_count.get)
print(most_sent, sender_count[most_sent])

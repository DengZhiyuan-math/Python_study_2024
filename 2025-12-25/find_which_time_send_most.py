sender_count = dict()
emails = open("mbox-short")
for line in emails:
    line = line.strip()
    if not line.startswith("From "):
        continue
    else:
        words = line.split( )
        hour = words[5].split(":")
        sender_count[hour[0]]= sender_count.get(hour[0],0) + 1

sorted_list_hours = sorted([(h, t) for h, t in sender_count.items()])
for hour, count in sorted_list_hours:
    print(hour, count)

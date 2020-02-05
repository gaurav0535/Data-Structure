import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

print(calls[0])
rec = {}

for a1,a2,a3,a4 in calls:
    if a1 not in rec:
        rec[a1] = int(a4)
    else:
        rec[a1] = int(rec[a1])+int(a4)

    if a2 not in rec:
        rec[a2] = int(a4)
    else:
        rec[a2] = int(rec[a1])+int(a4)



Keymax = max(rec, key=rec.get)

temp = "{} spent the longest time, {} seconds, on the phone during September 2016."
print(temp.format(Keymax,rec[Keymax]))
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
receiving_phone = []

for nos1,nos2,nos3,nos4 in calls:
    if(nos2  not in receiving_phone):
        receiving_phone.append(nos2)

for no1,no2,no3 in texts:
    if(no1 not in receiving_phone):
        receiving_phone.append(no1)

    if (no2 not in receiving_phone):
        receiving_phone.append(no2)

telemarketers = []

for n1,n2,n3,n4 in calls:
    if(n1  not in receiving_phone):
        telemarketers.append(n1)

print("These numbers could be telemarketers:")
for tele in telemarketers:
    print(tele)




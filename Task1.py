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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_phone_no = []

for phone_no in texts:
    if (phone_no[0] not in unique_phone_no):
        unique_phone_no.append(phone_no[0])

    if(phone_no[1] not in unique_phone_no):
        unique_phone_no.append(phone_no[1])

for phone_no_calls in calls:
    if (phone_no_calls[0] not in unique_phone_no):
        unique_phone_no.append(phone_no_calls[0])

    if (phone_no_calls[1] not in unique_phone_no):
        unique_phone_no.append(phone_no_calls[1])


print(f"There are {len(unique_phone_no)} different telephone numbers in the records.")




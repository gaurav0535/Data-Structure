"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
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

temp_phone = 0
temp_length = 0
for a1,a2,a3,a4 in calls:
    if(temp_length < int(a4)):
        temp_length = int(a4)
        temp_phone = a1

print("{} spent the longest time , {} seconds, on the phone during September 2016 ".format(temp_phone,temp_length))




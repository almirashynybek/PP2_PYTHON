#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
with open ('row.txt', 'r', encoding = 'utf - 8') as file:
    data = file.read()
def match(data):
    sequence = r'[A-Z][a-z]+'
    match = re.findall(sequence,data)
    print(match)

print(match(data))

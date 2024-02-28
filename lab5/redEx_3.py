#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
with open ('row.txt', 'r', encoding = 'utf - 8') as file:
    data = file.read()
def match(data):
    pattern = r'[a-n]+_[a-n]'
    match = re.findall(pattern,data)
    print(match)

print(match(data))

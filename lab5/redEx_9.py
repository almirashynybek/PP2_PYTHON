#Write a Python program to insert spaces between words starting with capital letters.
import re
with open ('row.txt', 'r', encoding = 'utf - 8') as file:
    data = file.read()
def match(data):
    sequence = r'(?<!^)(?=[A-Z])'
    match = re.sub(sequence,'',data)
    print(match)

print(match(data))

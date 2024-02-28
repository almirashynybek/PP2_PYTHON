#Write a Python program that matches a string that has an 'a' followed by two to three 'b'

import re
with open('row.txt','r', encoding = 'utf-8') as file:
    info = file.read()
mylist = []
words = info.split()
for i in words:
    match = re.search(r"a.b{2,3}", i)
    if match:
        mylist.append(match.group())
print(mylist)

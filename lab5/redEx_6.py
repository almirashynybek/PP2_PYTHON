#Write a Python program to replace all occurrences of space, comma, or dot with a colon

import re
with open('row.txt','r',encoding ='utf-8') as file:
    data = file.read()
mylist = []
cor = data.split()
for i in cor:
    match = re.search(r' .,',i)
    if match:
        mylist.append(match.group())
for i in mylist:
    print(':')




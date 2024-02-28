#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
with open('row.txt','r',encoding ='utf-8') as file:
    data = file.read()
mylist = []
cor = data.split()
for i in cor:
    match = re.search(r'a.*b',i)
    if match:
        mylist.append(match.group())
print(mylist)



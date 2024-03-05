import os
path = r"/Users/almirashynybek/Desktop/PP 2"

l = os.listdir(path)
print(l)

for root, dirs, files in os.walk(path):
    print(files)

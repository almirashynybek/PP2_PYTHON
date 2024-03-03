import os
if os.path.exists("Welcome.txt"):
    os.remove("Welcome.txt")
else:
    print("The file doesnot exist")
import string

for letter in string.ascii_uppercase:
    file_name = letter + ".txt"
    
    with open(file_name, "x") as f:
        f.write("This is file: " + file_name)
        print(f"File '{file_name}' has been created.")


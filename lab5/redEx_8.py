#Write a Python program to split a string at uppercase letters.
import re

def split_at_uppercase(s):
    # Use a regular expression to find all occurrences of uppercase letters followed by zero or more lowercase letters
    return re.findall(r'[A-Z][a-z]*', s)
string = input()
split_str = split_at_uppercase(string)

print(split_str)
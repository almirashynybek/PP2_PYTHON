#Write a Python program to convert a given camel case string to snake case.

import re

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()


camel_case_string = "ThisIsCamelCase"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)  # Output: this_is_camel_case
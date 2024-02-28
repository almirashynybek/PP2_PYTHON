#Write a python program to convert snake case string to camel case string.
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_str = components[0] + ''.join(x.title() for x in components[1:])
    return camel_str


snake_str = input()
print(snake_to_camel(snake_str))


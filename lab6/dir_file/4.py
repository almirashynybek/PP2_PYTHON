
with open("welcome.txt", "r") as f:
    line_count = 1
    line_count = sum(1 for line in f)

print( line_count)


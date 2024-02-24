def squares():
    for i in range (a, b):
        yield i**2

a = int(input())
b = int(input())
squar_num = squares()

for sq in squar_num:
    print(sq)
import math
def func(n):

    for i in range(n):
        yield i**2

n = int(input())
squares = func(n)

for sq in squares:
    print(sq)
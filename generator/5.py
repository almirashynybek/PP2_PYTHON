def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
down = countdown(n)

for num in down:
    print(num, end=" ")




def count_down(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
down = count_down(n)

for num in down:
    print(num)

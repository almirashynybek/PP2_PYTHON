def func(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

n = int(input())
even = func(n)

for even_num in even:
    print(even_num)
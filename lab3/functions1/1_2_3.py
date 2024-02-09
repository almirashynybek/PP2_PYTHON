def func(grams):
    ounces = 28.3495231 * grams
    return ounces
grams = int(input())
print(func(grams))


def func(F):
    return (5 / 9) * (F - 32) 
F = int(input())
print(func(F))

def solve(numheads, numlegs):
    c = (numlegs - 4*numheads)/-2
    r = numheads - c
    return f"rabits: {int(r)} \nchikens: {int(c)}"
print(solve(35,94))


from itertools import permutations

def permut(s):
    arr = permutations(s)
    return list(arr)

word=input()
result=permut(word)

print(result)
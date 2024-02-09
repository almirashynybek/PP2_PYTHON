def polind(s):
    if s==s[-1::-1]:
        return True
    return False
    
a=input()
result=polind(a)
print(result)
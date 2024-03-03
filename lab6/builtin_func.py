#1 
import math
def mult(x):
    return math.prod(x)
x = [2, 3, 5, 8, 3]
print(mult(x))


#2
s = "Welcome to Kazakhstan"
upper_count = sum(1 for char in s if char.isupper())
lower_count = sum(1 for char in s if char.islower())
print(upper_count, lower_count)


#3
s = str(input())
x = ''.join(reversed(s)) # convert reversed x into str
if x == s :
    print("Yes, it is polindrome")
else:
    print("No")

#4
import math
import time
def sqrt_time(n, milsec):
    time.sleep(milsec / 1000)
    num = math.sqrt(n)
    print(f"Square root of {n} after {milsec} milliseconds is {num}")
    return num
n = int(input())
milsec = int(input())
result = sqrt_time(n, milsec)


#5
def tupl(x):
    return all(x)
x = (True, True,1,1)
# x = (True, False, 1, 0)
print(tupl(x))

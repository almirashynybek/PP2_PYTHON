#1
import math
def func(x):
    rad = x * 3.14/180
    return rad
x = int(input())
print (func(x))


#2
def func():
    area = ((a + b) * h) / 2
    return area

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print(func())


#3
import math

def func():
    tan = math.tan(math.pi/n)
    area = (n * l * l) / 4 * tan 
    return area

n = int(input("Sides: "))
l = int(input("length of side: "))
print(func())


#4
def func():
    area = a * h
    return area

a = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
print(func())
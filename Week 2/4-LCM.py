# Uses python3
import sys

a,b = input().split()
a = int(a)
b = int(b)

def gcd_naive(x, y):
    if y == 0:
        return x
    else:
        return gcd_naive(y, x%y)

def LCM(x, y):
    lcm = (x*y)//gcd_naive(x,y)
    return lcm

print(LCM(a,b))

def easyline(n):
    # your codedef easyline(n):
    sum,value = 0,1
    for x in range(n+1):
        sum += value**2
        value = value * (n-x) // (x+1)
    return sum
print(easyline(4))

#best practices
from math import factorial
def easyline(n):
    return factorial(2*n) // (factorial(n)**2)
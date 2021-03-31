def divisors(n):
    x = 0
    i=1
    while(i<=n):
        if(n%i==0):
            x +=1
        i+=1
    return x
print(divisors(5))
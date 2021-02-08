def solutin(number):
    i = 1
    hasil = 0
    while(i < number):
        if(i % 3 == 0 or i % 5 == 0):
            hasil+=i
        i+=1
    return hasil

print(solutin(10))

#Clever
def solution1(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(solution1(10))
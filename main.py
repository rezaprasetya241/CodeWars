'''
def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

print(array_plus_array([1,2,3],[4,5,6]))
'''
'''
#if date = 24 and month = 12 it will be true
from datetime import date as waktu
def time_for_milk_and_cookies(dt):
    # your code heredef 
    # time_for_milk_and_cookies(dt):
    return dt.month == 12 and dt.day == 24
'''
'''
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

print(disemvowel("reza"))
'''
"""
#number
my_num = -5
print(type(my_num)) #se what type of yout variable
print(str(my_num))  #it will be change the type of variable from integer to string
print(str(my_num) + " my favorite number") # if you want to string after number,you must add str()
print(abs(my_num)) #to change from negative to positive
print(pow(my_num, 2)) #its ment my_num ^ 2
print(max(my_num, -10)) # to see maximum value betweens my_num and -10
print(min(my_num, -10)) #to see minimum value betweens my_num and -10
print(round(3.2)) #its for if (x>0.5) its going to 1 and if its x < 0.5 its going to 0
from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(4))
#end
"""
#Solution from codewars:
#def high_and_low(numbers):
#  n = map(int, numbers.split(" "))
#  return str(max(n)) + str(min(n))

# My soloution
'''
def high_and_low(number):
    n = map(int, number.split(" "))
    y = map(int, number.split(" "))
    return str(max(n)) + " " + str(min(y))
'''
#'''
# print(high_and_low("-213 6 -64 1 -3 542"))
#'''

'''
def get_sum(a,b):
    if a == b:
        return a
    elif a<b:
        n=0
        while(a<=b):
            n=a+n
            a =a+1
        return n
    elif b<a:
        n=0;
        while(b<=a):
            n=b+n
            b=b+1
        return n

print(get_sum(1, 0)) #== 1   // 1 + 0 = 1
print(get_sum(1, 2)) #== 3   // 1 + 2 = 3
print(get_sum(0, 1)) #== 1   // 0 + 1 = 1
print(get_sum(1, 1)) #== 1   // 1 Since both are same
print(get_sum(-1, 0)) #== -1 // -1 + 0 = -1
print(get_sum(-1, 2)) #== 2  // -1 + 0 + 1 + 2 = 
'''
#Codewars fundamental
'''
def xor(a,b):
    #your code here
    if a== True and b == True:
        return False
    elif a == False and b == False:
        return False
    elif a == True or b == False:
        return True
    elif a == False or b == True:
        return True
# Bisa di rankum hanya denga ndua baris
def xor(a,b):
    return a != b
'''
#end
#Does my number look big in this?
'''
def hitung_kuadrat(n):
    return n*n

bilangan = [1, 2, 3, 4, 5]
hasil = map(hitung_kuadrat, bilangan)
print(hasil)
print(list(hasil))
print(type(hasil))
'''
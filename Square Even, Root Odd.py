import math
def sum_square_even_root_odd(nums):
    # your code goes here
    sum = 0
    for x in nums:
        if(x%2==0):
            sum += x**2
        else:
            sum += math.sqrt(x) 
    return round(sum,2)
print(sum_square_even_root_odd([4,5,7,8,1,2,3,0]))
def create_array_of_tiers(n):
    # your awesome code here
    arr=list(str(n))
    word = str(n)
    for x in range(len(word)):
        if(x==0):
            arr[x] = arr[x]
        elif(x>0):
            arr[x] = arr[x-1]+arr[x]
    return arr

print(create_array_of_tiers(2019))
#best practice
from itertools import accumulate
def create_array(y):
    return list(accumulate(str(y)))
print(create_array(81091))


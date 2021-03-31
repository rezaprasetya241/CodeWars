def positive_sum(arr):
    # Your code here
    res = 0
    for x in arr:
        if(x>=0):
            res+=x
    return res

#clever
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
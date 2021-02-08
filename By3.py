def divisible_by_three(st): 
    # your code here
    st = int(st)
    if(st%3==0):
        return True
    else:
        return False
'''
#by clever
def divisible_by_three(s): 
    return int(s) % 3 == 0
'''
print(divisible_by_three("123"))
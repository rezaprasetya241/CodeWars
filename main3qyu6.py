# Made by me
'''
def narcissistic( value ):
    changeValue = list(map(int, str(value)))
    f = len(changeValue)
    res = 0
    for x in changeValue:
        res = ( x ** f) + res
    if(res != value):
        return False
    else:
        return True
'''
# Made by Clever(1)
#def narc(value):
    #return value == sum(int(x) ** len(str(value)) for x in str(value))
# Made by Clever(2)
#def narcis(value):
 #   return bool(value==sum([int(a) ** len(str(value)) for a in str(value)]))
def persistence(n):
    changeValue = list(map(int, str(n)))
    i = 0
    x = 0
    while(len(changeValue)!=1):
        f = changeValue[i] * changeValue[i+1]
        changeValue = list(map(int, str(f)))
        x +=1
    return x

print(persistence(39))
#=> 3  
# Because 3*9 = 27, 2*7 = 14, 1*4=4
# and 4 has only one digit.
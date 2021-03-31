def productFib(prod):
    arr = [0,1]
    i=0
    while(arr[-1]<=prod):
        arr.append(arr[i]+arr[i+1])
        i+=1
    for x in range(len(arr)-1):
        print(x)
        res = arr[x]*arr[x+1]
        if(res==prod):
            resproduct = True
            break
        elif(res>prod):
            resproduct = False
            break
    return [arr[x],arr[x+1],resproduct]
def productFib(prod):
    x,y = 0,1
    while(x*y<prod):
        temp = x
        x = y
        y += temp
    return [x,y, prod==x*y]
print(productFib(1))
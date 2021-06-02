def solve(arr):
    list1 = [list]
    # your code
    while(len(arr)==0):
        list1 = list1.append(arr[0:2])
        del arr[0:2]
    print(list1)
    return []
solve([1,2,3,4,5,6])




'''
solve([2, 1, 3, 4]) returns [2, 11] :
(2*2 + 1*1) * (3*3 + 4*4) = 5 * 25 = 125 and 2 * 2 + 11 * 11 = 125

solve([2, 1, 3, 4, 2, 2, 1, 5, 2, 3, 4, 5]) returns [2344, 2892] :
(2*2 + 1*1) * (3*3 + 4*4) * (2*2 + 2*2) * (1*1 + 5*5) * (2*2 + 3*3) * (4*4 + 5*5) = 13858000
and 2344 * 2344 + 2892 * 2892 = 13858000
'''
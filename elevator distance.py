def elevator_distance(array):
    res = 0
    for x in range(0, len(array)-1):
        res += abs(array[x]-array[x+1])
    return res
print(elevator_distance([7,1,7,1]))
def pathfinder_scores(scores):
    #happy coding
    x=0
    sum = 0
    for i in scores:
        if i<7 or i>18:
            return False
        else:
            if(i == 7):
                x = -4
            elif(i==8):
                x = -2
            elif(i==9):
                x = -1
            elif(i==10):
                x =0
            elif(i==11):
                x = 1
            elif(i==12):
                x = 2
            elif(i==13):
                x = 3
            elif(i==14):
                x = 5
            elif(i==15):
                x = 7
            elif(i==16):
                x=10
            elif(i==17):
                x = 13
            elif(i==18):
                x = 17
            sum +=x
    print(sum)
    if(sum>=1 and sum<=25):
        return True
    else:
        return False
            
print(pathfinder_scores([18, 13, 7, 12, 15, 10]))

#best Practice
PTS = dict(zip(range(7,19),(-4,-2,-1,0,1,2,3,5,7,10,13,17)))

def pathfinder(scores):
    return sum(PTS.get(x,float('inf')) for x in scores)<=25
print(pathfinder([18, 13, 7, 12, 15, 10]))
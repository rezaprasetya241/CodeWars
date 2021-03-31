def find_nb(m):
    # your code
    sum =0
    n = 1;
    while (sum<m):
        sum += n**3
        if(sum==m):
            return n
        n+=1
    return -1

#will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m 
print(find_nb(9)) #--> 45
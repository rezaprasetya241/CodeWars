def dbl_linear(n):
	# your code
    u = [1]
    i = 0
    j = 0
    while(len(u)<n+2):
        y = 2* u[i] + 1
        z = 3* u[j] + 1

        if y<z :
            u.append(y)
            i+=1;
        elif(y>z):
            u.append(z)
            j +=1
        else:
            u.append(y)
            i+=1
            j+=1
    u.sort()
    return u[n]
print(dbl_linear(10))
# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Example:
# u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

# Best Practices
def dbl_linear(n):
    u = [1]
    i = 0
    j = 0
    while len(u) <= n:
        x = 2 * u[i] + 1
        y = 3 * u[j] + 1
        if x <= y:
            i += 1
        if x >= y:
            j += 1
        u.append(min(x,y))
    return u[n]
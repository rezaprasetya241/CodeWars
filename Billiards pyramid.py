def pyramid(n):
    i = 1
    while i<= n:
        n = n -i
        i += 1
    return i-1
print(pyramid(4))

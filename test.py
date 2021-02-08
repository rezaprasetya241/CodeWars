def is_triangular(t):
    x = int ((t*2)**0.5)
    print(x)
    return t == x*(x+1)/2
print(is_triangular(3))
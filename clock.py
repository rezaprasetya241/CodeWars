
def past(h, m, s):
    h = h*3600000
    m = m*60000
    s = s*1000
    return h+m+s
print(past(0,1,1))


# clever
def past(h, m, s):
    return 3600000*h + m*60000 + s*1000
print(past(0,1,1))
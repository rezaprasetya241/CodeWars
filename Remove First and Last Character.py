def remove_char(s):
    x = list(s)
    del x[0], x[-1]
    return "".join(x)
print(remove_char("eloquent"))
#Clever
'''def remove_char(s):
    return s[1,-1]'''
def remove_char(s):
    res = slice(1,-1)
    return s[res]
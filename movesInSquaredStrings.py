# def vert_mirror(strng):
#     # your code
#     strng = strng.split()
#     arr = [i[::-1] for i in strng]
#     return '\n'.join(arr)
# def hor_mirror(strng):
#     x = strng.split()
#     x.reverse()
#     return '\n'.join(x)
# def oper(fct, s):
#     return fct(s)

# #best practices
# def vert_mirror(s):
#     return "\n".join(line[::-1] for line in s.split("\n"))

# def hor_mirror(s):
#     return "\n".join(s.split("\n")[::-1])

# def oper(fct, s):
#     return fct(s)
    
# # print(vert_mirror("abcd\nefgh\nijkl\nmnop"))
# print(oper(vert_mirror,"abcd\nefgh\nijkl\nmnop"))

# test.it("Basic tests vert_mirror")
# testing(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"), "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")
# testing(oper(vert_mirror, "IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"), "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")

# test.it("Basic tests hor_mirror")
# testing(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"), "yeCt\nCSbg\nJVhv\nlVHt")
# testing(oper(hor_mirror, "njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK")

# def alphanumeric(password):
#     if " " in password:
#         return False
#     else:
#         return password.isalnum()

# print(alphanumeric("S5zhvC"))
def to_underscore(string):
    # your code here
    res = ''
    string= str(string)
    for i in range(len(string)):
        x = string[i]
        bol = x.isupper()
        if(i==0):
            res+= string[i]
        elif(bol==True):
            res += '_'+string[i]
        else:
            res += string[i]
    return res.lower()
print(to_underscore(1))
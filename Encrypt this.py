def reverse(string):
    string = "".join(reversed(string))
    return string
'''def encrypt_this(text):
    arr = list(text)
    for x in range(len(arr)):
        if(x == 0 ):
            arr[x] = ord(arr[x])
        if(arr[x] == " "):
            arr[x+1] = ord(arr[x+1])
    res = ''.join(str(elem) for elem in arr)
    tmp = reverse(res)
    print(arr)
    print(res)
    print(tmp)
    pass
'''
def encrypt_this(text):
    arr = []
    stringlist = text.split(" ")
    for each in stringlist:
        firstLetter = str(ord(each[0]))
        each = reverse(each)
        s = firstLetter + each[0:-1]
        arr.append(s)
    return " ".join(arr)

def encrypt_this(text):
    res = []
    for word in text.split():
        word = list(word)
        word[0] = str(ord(word[0]))
        if(len(word)>2):
            word[1],word[-1] = word[-1],word[1] #for reverse
        res.append("".join(word))
    return " ".join(res)
print(encrypt_this("hello world"))
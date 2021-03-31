#by me
def expanded_form(num):
    arr = []
    lenNum = len(str(num))
    o = "0"
    divNum =int("1" + o*(lenNum-1))
    while(num!=0):
        res = str(num//divNum*divNum)
        num -= int(res)
        divNum //=10
        if(res!="0"):
            arr.append(res)
    return " + ".join(arr)

print(expanded_form(12)) #'10+2'
print(expanded_form(42)) #'40 + 2'
print(expanded_form(70304)) #'70000 + 300 + 4')

#best practice
def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)
print(expanded_form(70304))


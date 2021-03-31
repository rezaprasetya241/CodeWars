def calc(x):
    # your code here
    total1 = ""
    totalNum = 0
    totalNum2 = 0
    for i in x:
        convWord = ord(i)
        total1 = total1 + str(convWord)
    total2 = total1.replace("7","1")
    for i in total1:
        totalNum +=int(i)
    for i in total2:
        totalNum2 += int(i)
    return totalNum-totalNum2
print(calc("ABC"))

#Best practice
def calc(s):
    total1 = ''.join(map(lambda c: str(ord(c)), s))
    total2 = total1.replace('7', '1')
    return sum(map(int, total1)) - sum(map(int, total2))
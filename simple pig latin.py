def pig_it(text):
    res = []
    #your code here
    text = text.split(" ")
    for x in text:
        if len(x)==1:
            if x in "?!":
                res.append(x)
                continue
            tmp = x+"ay"
        else:
            i = list(x)
            i.append(x[0])
            del i[0]
            tmp = "".join(i)
            tmp = tmp+"ay"
        res.append(tmp)
    
    return " ".join(res)
print(pig_it("O tempora o mores !"))

# Best practices
# def pig_it(text):
#     res = []
    
#     for i in text.split():
#         if i.isalpha():
#             res.append(i[1:]+i[0]+'ay')
#         else:
#             res.append(i)
            
#     return ' '.join(res)
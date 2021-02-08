def solution(s):
    result = []
    if len(s) %2 == 1 :
        s +="_"
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
print(solution("hello"))

'''   
x =[s[i:i+2] for i in range(0,len(s),2)]
    n=0
word = 'CatBatSatFatOr'
print([word[i:i+3] for i in range(0, len(word), 3)]) 
'''
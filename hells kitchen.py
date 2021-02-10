def gordon(a):
    # your code here
    y= a.upper()
    v = y.maketrans("AIUEO","@****")
    z = y.translate(v)
    x = z.split(" ")
    for i in range(len(x)):
        x[i] = x[i] + "!!!!"
    return ' '.join(x)
print(gordon("whats app man"))
#best practice
def trans(q):
    return ' '.join(q.upper().split()).translate(str.maketrans("AIUEO","@****"))+"!!!!"
print(trans("Hello my name is allice"))
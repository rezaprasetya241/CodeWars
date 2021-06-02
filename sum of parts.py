def parts_sums(ls):
    # your code
    total = sum(ls)
    res = [total]
    for i in ls:
        res.append(total-i)
        total = total-i
    return res
print(parts_sums([0, 1, 3, 6, 10]))
#dotest([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0])

#Best Practices
def parts_sums(ls):
    result = [sum(ls)]
    for item in ls:
        result.append(result[-1]-item)
    return result
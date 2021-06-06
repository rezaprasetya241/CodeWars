from fractions import Fraction
def sum_fracts(lst):
    res = 0
    for i in lst:
        res += Fraction(i[0],i[1])
    total = str(res)
    if not lst:
        return None
    elif len(total) <=1:
        return int(total)
    else:
        total = total.split("/")
        return [int(total[0]),int(total[1])]

# test.assert_equals(sum_fracts([[1, 2], [1, 3], [1, 4]]), [13, 12]) 
# test.assert_equals(sum_fracts([[1, 3], [5, 3]]), 2) 

# best practice
# from fractions import Fraction

# def sum_fracts(lst):
#     if lst:
#         ret = sum(Fraction(a, b) for (a, b) in lst)
#         return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]

def get_count(n, x):
    # your code
    sisa=int(n/x)
    n=n-(sisa*x)
    return sisa,n

print(get_count(877692, 9))
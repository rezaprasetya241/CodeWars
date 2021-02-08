def solve(st,k):
    s = st
    for c in 'abcdefghijklmnopqrstuvwxyz':
        print(c)
        count = st.count(c)
        if count <= k:
            s = s.replace(c, '')
            k -= count
        else:
            s = s.replace(c, '', k)
            break
    return s
print(solve("abrakadabra",6))
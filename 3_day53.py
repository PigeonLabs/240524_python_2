def solution(n):
    res = []
    i = 2
    while i<=n:
        if n%i==0:
            n /= i
            if not i in res:
                res.append(i)
        else:
            i += 1
    return res
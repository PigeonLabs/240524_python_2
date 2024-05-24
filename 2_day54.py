num, res = set(), set()
for n in range(2,1000001):
    c = True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            c = False
            continue
    if c == True:
        num.add(n)
a = num.copy()
while a:
    tnum = set()
    t = str(a.pop())
    for _ in range(len(t)):
        t = t[-1:]+t[:-1]
        tnum.add(int(t))
    if len(tnum&num)==len(tnum):
        res.update(tnum)
    a -= tnum
print(len(res)) #55
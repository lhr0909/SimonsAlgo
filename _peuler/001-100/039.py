m = 0
ans = 0
for p in range(3,1001):
    s = 0
    for a in range(1,p):
        for b in range(a+1,p-a):
            c1 = a*a + b*b
            c2 = (p-a-b)*(p-a-b)
            if c1==c2:
                s = s + 1
    if s>m:
        m = s
        ans = p
        print m, ans

print ans

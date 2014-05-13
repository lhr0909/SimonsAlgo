def sieve(n):
    li = [True] * n
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            for j in range(i*i, n, i):
                li[j] = False
    return li

count = 0
li = sieve(1000000)
ans = []
for i in range(11, len(li)):
    if li[i]==True:
        temp = str(i)
        k = 0
        for j in range(1, len(temp)):
            a = temp[j:]
            b = temp[:-j]
            if (li[int(a)]==True)and(li[int(b)]==True):
                k = k + 2
        if k==(len(temp) - 1) * 2:
            ans.append(i)
print ans
print sum(ans)           

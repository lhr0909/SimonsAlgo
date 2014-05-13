list = ['1','2','3','4','5','6','7','8','9']
ans = set()
for i in range(2, 50):
    if (i % 11==0)or(i % 10==0):
        continue
    for j in range(10000 / i,123,-1):
        li = []
        k = i * j
        li.extend(sorted(str(i)))
        li.extend(sorted(str(j)))
        li.extend(sorted(str(k)))
        li = sorted(li)
        if li==list:
            ans.add(k)
            print "%d * %d = %d" % (i,j,k)
print sum(ans)
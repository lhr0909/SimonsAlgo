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
ans = set()
for i in range(len(li)):
    if li[i]==True:
        if i<=10:
            ans.add(i)
        else:
            temp = str(i)
            templi = []
            for j in range(len(temp)):
                temp = temp[-1:] + temp[:-1]
                if li[int(temp)]==True:
                    templi.append(int(temp))
                else:
                    break
            if len(templi)==len(str(i)):
                for item2 in templi:
                    ans.add(item2)
                
print len(ans)

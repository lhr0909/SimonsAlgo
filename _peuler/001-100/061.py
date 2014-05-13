p = [0, 0, 0]
p.append(lambda n: n*(n+1)/2)   #p[3]
p.append(lambda n: n*n)         #p[4]
p.append(lambda n: n*(3*n-1)/2) #p[5]
p.append(lambda n: n*(2*n-1))   #p[6]
p.append(lambda n: n*(5*n-3)/2) #p[7]
p.append(lambda n: n*(3*n-2))   #p[8]

a = [0, 0, 0]
for i in xrange(3, 9):
    a.append([])
    j = 1
    temp = p[i](j)
    while temp < 10000:
        if temp >= 1000:
            a[i].append(temp)
        j += 1
        temp = p[i](j)

first2 = [0, 0, 0]
last2 = [0, 0, 0]
for i in xrange(3, 9): 
    first2.append(map(lambda x: str(x)[0:2], a[i]))
    last2.append(map(lambda x: str(x)[2:4], a[i]))

def listRemove(item, ls):
    ans = []
    for i in ls:
        if i != item:
            ans.append(i)
    return ans

def listAdd(item, ls):
    ans = []
    for i in ls:
        ans.append(i)
    ans.append(item)
    return ans

def findSequence(s, t):
    for i in t:
        for j in xrange(len(a[i])):
            if len(s) == 0:
                ns = listAdd([a[i][j], i, j], s)
                nt = listRemove(i, t)
                if findSequence(ns, nt):
                    return True
            else:
                pa = s[len(s)-1] #previous number
                pi = pa[1]
                pj = pa[2]
                if last2[pi][pj] == first2[i][j]:
                    if len(t) == 1:
                        fa = s[0] #first number
                        fi = fa[1]
                        fj = fa[2]
                        if last2[i][j] == first2[fi][fj]: #found answer
                            ans = listAdd([a[i][j], i, j], s)
                            print ans
                            ans = sum(map(lambda x: x[0], ans))
                            print ans
                            return True
                    else:
                        ns = listAdd([a[i][j], i, j], s)
                        nt = listRemove(i, t)
                        if findSequence(ns, nt):
                            return True
    return False

findSequence([], range(3, 9))
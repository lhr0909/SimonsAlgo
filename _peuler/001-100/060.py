from MathLib import makePrimes, isPrime

p = makePrimes(10000)
sp = set(p)

def listAdd(item, ls):
    ans = []
    for i in ls:
        ans.append(i)
    ans.append(item)
    return ans

def findPrimes(a):
    for i in p:
        if len(a) == 0:
            if findPrimes(listAdd(i, a)):
                return True
        else:
            if i not in a:
                count = 0
                for j in a:
                    m = int(str(i)+str(j))
                    n = int(str(j)+str(i))
                    if m in sp or isPrime(m):
                        if n in sp or isPrime(n):
                            count += 1
                if count == len(a):
                    if len(a) == 4:
                        ans = listAdd(i, a)
                        print ans
                        print sum(ans)
                        return True
                    else:
                        if findPrimes(listAdd(i, a)):
                            return True
    return False

findPrimes([])
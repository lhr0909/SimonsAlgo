#Related problem: 034

from math import factorial

def getNext(n):
    ans = 0
    for digit in str(n):
        ans += factorial(int(digit))
    return ans

#Crazy memoization, runs in 26 secs. 
count = 0
lookUp = dict()
for i in xrange(1, 10**6):
    chain = []
    temp = i
    while temp not in chain:
        if temp in lookUp:
            chain.extend(lookUp[temp])
            break
        else:
            chain.append(temp)
            temp = getNext(temp)
    n = len(chain)
    if n == 60:
        count += 1
    x = getNext(chain[n-1])
    for j in xrange(chain.index(x) + 1):
        if chain[j] not in lookUp:
            lookUp[chain[j]] = chain[j:]
            
print count

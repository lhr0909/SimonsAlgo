def sieve(n):
    li = [True] * n
    primes = []
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            primes.append(i)
            for j in range(i*i, n, i):
                li[j] = False
    return primes

def binaryGenerator(num, bit):
    bits = []
    k = num
    while k > 0:
        bits.insert(0, k % 2)
        k /= 2
    for i in range(len(bits), bit):
        bits.insert(0, 0)
    return bits
    
def checkZeroes(bitgen):
    zero = []
    one = []
    for i in range(len(bitgen)):
        if bitgen[i]==1:
            one.append(i)
        else:
            zero.append(i)
    return zero, one
    
def numberGenerator(nums, repeat, zeroPos, onePos):
    n = list(digit for digit in str(nums))
    for i in range(len(n), len(zeroPos)):
        n = ['0'] + n
    ret = ['0'] * (len(zeroPos) + len(onePos))
    for i in range(len(n)):
        ret[zeroPos[i]] = n[i]
    for i in range(len(onePos)):
        ret[onePos[i]] = str(repeat)
    return ret
    
            
    
d = 6
p = sieve(10**d)
s = set(p)
ans = [10**d, 1]
for i in range(1, 2**(d-1)):
    q = binaryGenerator(i, d-1) + [0]
    zeroPos, onePos = checkZeroes(q)
    for j in range(10**len(zeroPos)):
        if str(j)[len(str(j))-1] in set(['1','3','7','9']):     #last digit has to be 1, 3, 7, 9
            primeCount = 0
            failCount = 0
            firstPrime = True
            f = []
            for k in range(10):
                pattern = numberGenerator(j, k, zeroPos, onePos)
                if int(''.join(pattern)) in s:
                    if firstPrime:
                        f = pattern
                        firstPrime = False
                    primeCount += 1
                else:
                    failCount += 1
                if failCount > 2:    #if it fails more than 2 times, break
                    break
            if primeCount >= ans[1]:
                if f[0] != '0':
                    if primeCount==ans[1]:
                        if int(''.join(f))<ans[0]:
                            ans = [int(''.join(f)), primeCount]
                    else:
                        ans = [int(''.join(f)), primeCount]
            
print ans

    
    
    
        

from MathLib import isPrime, nextPrime

ans = 10

for i in xrange(11, 150 * pow(10, 6)):
    j = i * i + 1
    if isPrime(j):
        if nextPrime(j) == j + 2:
            j += 2
            if nextPrime(j) == j + 4:
                j += 4
                if nextPrime(j) == j + 2:
                    j += 2
                    if nextPrime(j) == j + 4:
                        j += 4
                        if nextPrime(j) == j + 14:
                            print i, 
                            ans += i
                            print ans
                            
print ans
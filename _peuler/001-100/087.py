from MathLib import makePrimes

p = makePrimes(7100)

ansS = set()

count = 0
limit = 5 * pow(10, 7)
for i in p:
    m = pow(i, 4)
    if m <= limit:
        for j in p:
            n = pow(j, 3)
            if m + n <= limit:
                for k in p:
                    o = pow(k, 2)
                    s = m + n + o
                    if s <= limit:
                        print "%d = %d^2 + %d^3 + %d^4" % (s, k, j, i)
                        #Beware of the duplicates
                        ansS.add(s)
print len(ansS)
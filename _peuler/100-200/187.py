#http://mathworld.wolfram.com/Semiprime.html
#http://en.wikipedia.org/wiki/Prime-counting_function

#The answer is a sum of pi(n/i) - pi(i) + 1 for all prime i not greater than sqrt(n). 

from MathLib import makePrimes

n = pow(10, 8)
p = makePrimes(n / 2)

#print len(p)

s = 0

for i in xrange(len(p)):
    for j in xrange(i, len(p)):
        if p[i] * p[j] < n:
            s += 1
        else:
            break

print s
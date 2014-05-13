#Related Problems: Project Euler 108

#Since the maximum number of primes used to produce more than 4 million answer
#should be less than 25. Since 2^23 > 8 million

#So I used a partition iterator to find all the partitions from 1 to 25.
#That only contains about 7337 iterations
#And then just calculated through

#Special Thanks to inamori for the post online,
#and Daniel Kahl (Freshman '14 at Rose) for translation of the post.

#Solves in 0.063s. AWESOME!

#http://d.hatena.ne.jp/inamori/20100625/p1

#inamori has another post for getting the answer using Lagrange Multipliers.
#Still don't know what is going on.

#http://d.hatena.ne.jp/inamori/20100627/p1

from MathLib import partition_iter, product, makePrimes

p = makePrimes(100)

limit = 4 * pow(10, 6)

minimum = pow(10, 100)

count = 0

for i in xrange(1, 25):
    for j in partition_iter(i):
        count += 1
        l = list(j)
        l.reverse()
        m = (product(map(lambda x: 2 * x + 1, l)) + 1) / 2
        if m > limit:
            s = 1
            for k in xrange(len(l)):
                s *= pow(p[k], l[k])
            if s < minimum:
                minimum = s

print count
print minimum
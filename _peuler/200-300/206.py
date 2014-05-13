import sys
from math import sqrt

for d1 in xrange(10):
    for d2 in xrange(10):
        for d3 in xrange(10):
            for d4 in xrange(10):
                for d5 in xrange(10):
                    for d6 in xrange(10):
                        for d7 in xrange(10):
                            for d8 in [0, 4, 8]:
                                    a = 1020304050607080900
                                    a += d1 * 100000000000000000
                                    a += d2 * 1000000000000000
                                    a += d3 * 10000000000000
                                    a += d4 * 100000000000
                                    a += d5 * 1000000000
                                    a += d6 * 10000000
                                    a += d7 * 100000
                                    a += d8 * 1000
                                    #print a
                                    k = int(sqrt(a) + 0.5)
                                    if k * k == a:
                                        print k
                                        sys.exit(0)
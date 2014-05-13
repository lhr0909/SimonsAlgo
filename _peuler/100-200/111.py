#A lot of generating issues...
#http://d.hatena.ne.jp/inamori/20100628/p1
#just checked the answer with him though... Implemented pretty much myself
#runs faster than his.

from MathLib import choose_iter, isPrime

mnd = dict()
mnd[4] = [2, 3, 3, 3, 3, 3, 3, 3, 3, 3]
mnd[10] = [8, 9, 8, 9, 9, 9, 9, 9, 8, 9]

def repeatPrime(n, d):
    if d == 0:
        for i in choose_iter(range(1, n - 1), mnd[n][0]):
            for j in xrange(10, 100):
                s = ''
                x = str(j / 10)
                y = str(j % 10)
                first = True
                for k in xrange(n):
                    if k in i:
                        s += '0'
                    else:
                        if first:
                            s += x
                            first = False
                        else:
                            s += y
                s = int(s)
                if isPrime(s):
                    yield s
    else:
        x = n - mnd[n][d]
        for i in choose_iter(range(n), x):
            if x == 2:
                f = range(pow(10, x))
            else:
                f = range(pow(10, x - 1), pow(10, x))
            for j in f:
                if x == 2:
                    y = '%02d' % j
                else:
                    y = str(j)
                ind = 0
                s = ''
                for k in xrange(n):
                    if k in i:
                        s += y[ind]
                        ind += 1
                    else:
                        s += str(d)
                if s[0] == '0':
                    continue
                s = int(s)
                if isPrime(s):
                    yield s

n = 10
ans = 0

for d in xrange(10):
    j = 0
    for i in repeatPrime(n, d):
        #print i
        ans += i
        j += 1
    #print j

print ans


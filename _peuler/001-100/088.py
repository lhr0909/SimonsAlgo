#http://d.hatena.ne.jp/inamori/20100219/p1
#http://www.research.att.com/~njas/sequences/A104173
#Need some revision, runs in 50 mins.

#I can now call maple for help on numbers in Python, just to shorten some time.

#but should try Pexpect next time whenever I have a chance using Maple again.
#http://www.noah.org/wiki/Pexpect
#after testing, Pexpect is not as fast as subprocess... But it is SAFER...
#Pexpect is SO SLOW... Give up.

#I added a handling trick: Every time I run a Maple Command,
#I attached a "EndofLine;" Command, which in Maple will just
#regard that as a symbol, returning just a line with "EndofLine"
#fixed the reading problem. (Hopefully did not hurt the performance)

#Should have thought more about the numbers first
#euler's method in the forum is very cool and straightforward

#had a lot of troubles generating the products list
#(that's all why it took me forever to find out)

#learned how to use yield and recursion on yield (cool stuff)

from MathLib import isPrime

#Maple initializations
#subprocess version
from subprocess import Popen, PIPE
maple = Popen(['maple', '-t', '-u', '-q'], stdin=PIPE, stdout=PIPE, stderr=None, close_fds=True)
#use numtheory package to find divisors of a number
maple.stdin.write('with(numtheory):\n')
'''
#Pexpect version (SLOW)
import pexpect
maple = pexpect.spawn('maple -t -u')
maple.expect('#-->')
maple.sendline('with(numtheory):')
maple.expect('#-->')
'''

def ask_maple(command):
    #subprocess version
    #can be easily deadlocked if calling stdout.readline() more than
    #the output actually has
    maple.stdin.write(command + ';EndofLine;\n')
    t = ""
    t = maple.stdout.readline().strip()
    k = maple.stdout.readline().strip()
    while k !='EndofLine':
        t += k
        k = maple.stdout.readline().strip()
    return t
    '''
    #Pexpect version (SLOW)
    maple.sendline(command + ';')
    maple.expect('#-->')
    out = maple.before
    out = out[out.index(';')+1:].strip()
    out = ''.join(out.split('\r\n'))
    return out
    '''

def divisors(n):
    t = ask_maple('divisors(%d)' % n)
    t = t.replace('{', '[').replace('}', ']').replace('\n', '')
    return eval(t)[1:-1]

def primeFactors(n):
    pf = eval(ask_maple('ifactors(%d)' % n))[1]
    factors = []
    for item in pf:
        for i in xrange(item[1]):
            factors.append(item[0])
    return factors

def product(ls):
    m = 1
    for item in ls:
        m *= item
    return m

def findProductPairs(n, d):
    for i in xrange(len(d) / 2 + 1):
        yield tuple(sorted([d[i], d[len(d) - 1 - i]]))

def findProduct(n, k, pf, d):
    if k == len(pf):
        yield tuple(pf)
    elif k == 2:
        for item in findProductPairs(n, d):
            yield item
    elif k > 2 and k < len(pf):
        for item in findProduct(n, k - 1, pf, d):
            t = tuple(item[:-1])
            p = item[-1]
            dSub = divisors(p)
            if len(dSub) > 0: #make sure it is not prime
                for temp in findProductPairs(p, dSub):
                    yield tuple(sorted(t + temp)) 

def findProducts(n):
    pf = primeFactors(n)
    d = divisors(n)
    s = set()
    for i in xrange(2, len(pf)+1):
        for item in findProduct(n, i, pf, d):
            s.add(item)
    return list(s)

n = 100

r = dict()
for i in xrange(4, 150+1):
    if not isPrime(i):
        t = findProducts(i)
        for item in t:
            k = len(item) + (i - sum(item))
            if k not in r:
                r[k] = i
            else:
                if i < r[k]:
                    r[k] = i
            print i, k, r[k]

s = set()
for i in xrange(2, n + 1):
    s.add(r[i])
print sum(s)
maple.terminate()
#if k is prime,
#m(k) = m(k - 1) + 1
#
#if k is not prime,
#prime factorize k = p1^e1 * p2^e2 * ... * pn^en
#m(k) = e1*m(p1) + e2*m(p2) + ... + en*m(pn)
#see if it works
#Well, probably not, even if it seems to work for anything less than 20
#but there is another thing that I found out earlier
#m(k) = m(k / 2) + 1 ---- if k is even
#m(k) = m(k - 1) + 1 ---- if k is odd
#see if this works
#FUCK, 2 off from correct answer!
#it was m(77) = 8, but mine was m(77) = 9
#and so it makes m(154) off by 1 as well
#I knew my method was not optimum, but I want to know how to do it.
#
#IT NEEDS TO BE REDONE
#two websites:
#http://www.imc.pi.cnr.it/resta/ac/fr00.html
#http://d.hatena.ne.jp/inamori/20090514/p2
#http://d.hatena.ne.jp/inamori/20080330

#http://wonderfl.net/c/2oNO

#After reading the forum, I found out the factor method actually works.
#don't even have to prime factorize a number.
#http://www.research.att.com/~njas/sequences/a003313.txt
'''
l(1) = 0; if n is prime l(n)=l(n-1)+1;
else {n=j*k j,k>1; l(k*j)=l(k)+l(j)},
'''

md = dict()
md[1] = (0, [1])

def m(k):
    if k in md:
        return md[k][0]
    else:
        smallest = k
        smallestI = 1
        smallestX = []
        for i in xrange(1, k):
            x = md[i][1][:]
            for j in x:
                if i + j == k:
                    if md[i][0] + 1 < smallest:
                        print i
                        smallest = md[i][0] + 1
                        smallestI = i
                        smallestX = x[:]
        smallestX.append(k)
        md[k] = (smallest, smallestX)
        return md[k][0]

ans = 0
for i in xrange(1, 201):
    ans += m(i)
    print i, md[i]

print ans - 2
#right now, m(77) and m(154) are off by 1.
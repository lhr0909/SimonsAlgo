#http://erl.nfshost.com/2008/03/02/euler-100/
#http://www.research.att.com/~njas/sequence/A011900
#should have used OEIS (online encyclopedia of integer sequence)...

'''
Solve using Pell Equation

[a / (a + b)] * [(a - 1) / (a + b - 1)] = 1/2

solve for a as a function of b

a = (B + A + 1) / 2

where:
B = 2*b
A^2 = 2*B^2 + 1

Solve for A and B in the Pell equation A^2 - 2*B^2 = 1
'''

a = dict()

a[0] = 1
a[1] = 3
i = 1
while 2*a[i]*(a[i]-1) <= pow(10, 24):
    i += 1
    a[i] = 6 * a[i-1] - a[i-2] - 2

print a[i]

"""
def findHalf(n):
    s = set()
    left = 2
    right = n
    mid = (left + right) / 2
    a = mid*(mid-1)
    b = n*(n-1)
    if (b / 2) % 2 == 1:
        return False
    else:
        while b != 2*a:
            s.add(mid)
            if 2*a > b:
                right = mid
            else:
                left = mid
            mid = (left + right) / 2
            if mid in s:
                return False
            a = mid*(mid-1)
        return mid

'''
4 3 1
21 15 6
120 85 35
697 493 204
4060 2871 1189
23661 16731 6930
137904 97513 40391
803761 568345 235416
4684660 3312555 1372105
'''

count = 0
i = 3
while count < 5:
    k = findHalf(i)
    if k != False:
        print i, k, i-k
        count += 1
    i += 1

#count = 0
#i = pow(10, 12) + 147100000
#while count < 1:
#    if i % 100000 == 0:
#        print i
#    k = findHalf(i)
#    if k != False:
#        print i, k, i-k
#        count += 1
#    i += 1
"""
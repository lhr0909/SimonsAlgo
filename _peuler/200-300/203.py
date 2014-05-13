p = [2, 3, 5, 7, 11, 13, 17, 19]
p = map(lambda x: x * x, p)
c = dict()
s = set()

n = 51
c[(0, 0)] = 1
c[(1, 0)] = 1
c[(1, 1)] = 1
s.add(1)
ans = 1

for i in xrange(2, n):
    c[(i, 0)] = 1
    for j in xrange(1, i):
        c[(i, j)] = c[(i - 1, j - 1)] + c[(i - 1, j)]
        if c[(i, j)] not in s:
            m = 0
            for k in p:
                if c[(i, j)] % k != 0:
                    m += 1
            if m == len(p):
                ans += c[(i, j)]
                s.add(c[(i, j)])
    c[(i, i)] = 1

print ans

#http://blog.dreamshire.com/2009/04/20/project-euler-problem-204-solution/

'''
Only a few primes are required.
For example, 51! is the biggest numerator (nCk = n! / k! (n-k)! )
and the largest prime factor required is ≤ √51 which is 7.
We added a few more to try bigger problems.

So we fill a hash’s keys with unique numbers from Pascal’s triangle
and iterate through the 589 binomial coefficients
and track which ones are squarefree,
sum them up and print the results.
'''
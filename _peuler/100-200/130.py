#Related Problems: 129

from MathLib import isPrime

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def A(n):
  if isPrime(n) or gcd(n, 10) != 1: return None
  x, k = 1, 1
  while x != 0:
    x = (x*10+1) % n #saves a lot of time
    k += 1
  return k

s = [91, 259, 451, 481, 703]
n = s[-1]
while len(s)< 25:
  n += 2
  an = A(n)
  if an != None and (n-1) % an == 0: 
    s.append(n)
 
print sum(s)
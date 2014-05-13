#Related Problem: Project Euler 132 133

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def A(n):
  if gcd(n, 10) != 1: return None
  x, k = 1, 1
  while x != 0:
    x = (x*10+1) % n #saves a lot of time
    k += 1
  return k

#start from 1000001
limit = 1000001
n = limit
while A(n)<limit: n += 2

print n
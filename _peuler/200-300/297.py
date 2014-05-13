p = 17
k = pow(10, p)
 
#fibonacci generator
fib = dict()
fib[0] = 1
fib[1] = 1
i = 1
while fib[i] < k:
    i += 1
    fib[i] = fib[i-1] + fib[i-2]
del fib[i]
 
def Zeckendorf(n):
    #return the Zeckendorf partition as a sequence
    k = n
    s = []
    for key in xrange(len(fib)-1, -1, -1):
        if fib[key] <= k:
            s.append(fib[key])
            k = k - fib[key]
            if k == 0:
                break
    return s
 
#get the Zeckendorf partition for the destination
zek = Zeckendorf(k)
 
#recurrence relations
a = dict()
a[1] = 0
a[2] = 1
s = dict()
s[1] = 0
s[2] = 1
for i in xrange(3, len(fib)):
    a[fib[i]] = fib[i-1] + s[fib[i-1]]
    s[fib[i]] = a[fib[i-1]] + s[fib[i-1]]
 
#get the final count
s[k] = s[zek[0]]
j = 1
for i in zek[1:]:
    s[k] += j*i + s[i]
    j += 1
 
#and BAM!
print s[k]

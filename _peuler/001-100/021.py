def amicable(n):
    s = 0
    for i in range(1, n):
        if (n % i==0)and(i<n):
            s = s + i
    return s



sum = 0
list = [False] * 20000
for i in range(10000):
    if (amicable(amicable(i))==i)and(i!=amicable(i)):
        sum = sum + i
print sum
        

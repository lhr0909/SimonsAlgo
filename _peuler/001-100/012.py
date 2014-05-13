

def primes(m):
    li = []
    n = m + 1
    li = [True] * n
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            for j in range(i*i, n, i):
                li[j] = False
    return li


li = primes(50000000)


def divisors(m):
    divisor = []
    n = m
    count = 2
    while count<=n:
        temp = 0
        while (li[count])and(n % count==0):
            temp = temp + 1
            n = n / count
        if temp!=0:
            divisor.append(temp)
        count = count + 1
    product = 1
    for item in divisor:
        product = product * (item + 1)
    return product

sum = 0
i = 1
while 1:
    sum = sum + i
    temp = divisors(sum)
    #print i, sum, temp
    if temp>500:
        break
    i = i + 1
print "answer:", sum
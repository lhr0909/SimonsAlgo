#all permutations: from 024.py

number = [0,1,2,3,4,5,6,7,8,9]
#print number
n = 10
primes = [2,3,5,7,11,13,17]
s = 0

for a in range(10*9*8*7*6*5*4*3*2):
    i = n - 1
    while number[i-1]>=number[i]:
        i = i - 1
    j = n
    while number[j-1]<=number[i-1]:
        j = j - 1
    number[i-1], number[j-1] = number[j-1], number[i-1]
    i = i + 1
    j = n
    while i<j:
        number[i-1], number[j-1] = number[j-1], number[i-1]
        i = i + 1
        j = j - 1
    propCount = 0
    for k in range(1, 8):
        prop = (number[k] * 100 + number[k+1] * 10 + number[k+2]) % primes[k-1]
        if prop==0:
            propCount += 1
    if propCount>=7:
        s += sum([number[i] * (10**(9-i)) for i in range(10)])

print s

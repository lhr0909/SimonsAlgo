'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
'''
a = 20 * 19 * 9 * 17 * 4 * 7 * 13 * 11
print a
'''
k = 0
for i in range(1, 21):
    if a % i==0:
        k = k + 1
print k
'''

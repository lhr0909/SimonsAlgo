'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

largest = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        k = i * j
        if k>=100000:
            if ((k % 10)==(k / 100000))and(((k % 100) / 10)==((k / 10000) % 10))and(((k % 1000) / 100)==((k / 1000) % 10)):
                if k>=largest:
                    largest = k
print largest

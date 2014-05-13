'''
d(1) = 1
d(10) = 1
d(100) = 5
d(1000) = 3
d(10000) = 7
d(100000) = 2
d(1000000) = 1

1 digit number: 9*1  (1-9)
Cumulative: 9

2 digit number: 90*2 (10-99)
we need 91 digits, which will be after 45 terms, 10 + 45 = 55
it will be the first digit of 56, which is 5.
Cumulative: 189

3 digit number: 900*3 (100-999)
we need 811 digits, which will be after 270 terms, 100 + 270 = 370
it will be the first digit of 371, which is 3.
Cumulative: 2889

4 digit number: 9000*4 (1000-9999)
we need 7111 digits, which will be after 1777 terms, 1000 + 1777 = 2777
it will be the third digit of 2778, which is 7.
Cumulative: 38889

5 digit number: 90000*5 (10000-99999)
we need 61111 digits, which will be after 12222 terms, 10000 + 12222 = 22222
it will be the first digit of 22223, which is 2.
Cumulative: 488889

6 digit number: 900000*6 (100000-999999)
we need 511111 digits, which will be after 85185 terms, 100000 + 85185 = 185185
it will be the first digit of 185186, which is 1.
'''

j = 9
k = 10
ans = 1
for i in range(2, 7):
     print j,
     m = (k * 10 - j) % i
     n = k + (k * 10 - j)/i
     if m > 0:
          print n + 1, str(n + 1)[m-1]
          ans *= int(str(n + 1)[m-1])
     else:
          print n, str(n)[i-1]
          ans *= int(str(n)[i-1])
     j = j + k * 9 * i
     k = k * 10
print ans

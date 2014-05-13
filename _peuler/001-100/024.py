#http://www.cut-the-knot.org/do_you_know/AllPerm.shtml

number = [0,1,2,3,4,5,6,7,8,9]
#print number
n = 10


for a in range(999999):
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
    #print number
print number

ans = 0
for i in range(2, 354294):
    temp = "%07d" % i
    if sum(int(digit)**5 for digit in temp)==int(temp):
        ans = ans + i
        print i
print "Answer:", ans
print sum(int(digit) for digit in str(2**1000))  #cheating!!!

sum = '2'
for n in range(999):
    digit = '0'
    temp = ''
    for i in range(len(sum)):
        temp = temp + str((int(sum[i]) + int(sum[i]) + int(digit)) % 10)
        digit = str((int(sum[i]) + int(sum[i]) + int(digit)) / 10)
    sum = temp
    if digit!='0':
        sum = sum + digit
sod = 0
for i in range(len(sum)):
    sod = sod + int(sum[i])
print sod

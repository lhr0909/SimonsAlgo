#continued fraction
#convergent

#continued fraction of e: [2; 1, 2, 1, 1, 4, 1, ..., 1, 2k, 1]

#initialization
h_2 = 0
h_1 = 1
h = 2*h_1 + h_2
h_2 = h_1
h_1 = h
i = 2
count = 1
n = 100
#loop
while count <= n:
    #print h
    count += 1
    h = 1*h_1 + h_2
    h_2 = h_1
    h_1 = h
    if count >= n: break
    #print h
    count += 1
    h = i*h_1 + h_2
    h_2 = h_1
    h_1 = h
    i += 2
    if count >= n: break
    #print h
    count += 1
    h = 1*h_1 + h_2
    h_2 = h_1
    h_1 = h
    if count >= n: break
    
#print h
print sum(map(int, str(h)))
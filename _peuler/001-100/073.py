#Stern-Brocot Tree
#Calkin-Wilf Tree -- extended knowledge
#related problems: 071,  072

##stack overflow
##def binaryExpandRec(L, R, n):
##    M = mediant(L, R)
##    if M[0] < M[1] and M[1] <= n:
##        return 1 + binaryExpand(L, M, n) + binaryExpand(M, R, n)
##    else:
##        return 0

#And REMEMBER: you NEVER want to use nested lists and len() if you don't need to. makes your life so much easier!
def binaryExpand(L, R, n):
    count = 0
    lastCount = -1
    numer = [L[0], R[0]]
    denom = [L[1], R[1]]
    listLen = 2
    while True:
        i = 1
        while i < listLen:
            Mnumer = numer[i-1] + numer[i]
            Mdenom = denom[i-1] + denom[i]
            if Mnumer < Mdenom and Mdenom <= n:
                numer.insert(i, Mnumer)
                denom.insert(i, Mdenom)
                listLen += 1
                count += 1
            else:
                i += 1
        if lastCount == count:
            break
        else:
            lastCount = count
    return count
    
#print binaryExpandRec([1, 3], [1, 2], 400)
print binaryExpand([1, 3], [1, 2], 12000)

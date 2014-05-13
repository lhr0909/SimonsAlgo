coins = [0,1,2,5,10,20,50,100,200]


def find(n,k):
    if (k<1)or(n<0):
        return 0
    elif n==0:
        return 1
    else:
        return find(n,k-1)+find(n-coins[k],k)

print find(200,8)

#http://stackoverflow.com/questions/1106929/find-all-combinations-of-coins-when-given-some-dollar-value
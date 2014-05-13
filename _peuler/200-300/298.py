from random import randint

Larry = dict()
Robin = dict()
lScore = 0
rScore = 0

def LarryPlays(number):
    global Larry
    global lScore
    if number in Larry:
        lScore += 1
    for i in Larry.keys():
        Larry[i] += 1
    if len(Larry) == 5:
        m = 0
        x = 0
        for i in Larry.keys():
            if Larry[i] > m:
                m = Larry[i]
                x = i
        del Larry[x]
    Larry[number] = 1
    #print sorted(Larry.keys()), lScore

def RobinPlays(number):
    global Robin
    global rScore
    if number in Robin:
        rScore += 1
    for i in Robin.keys():
        Robin[i] += 1
    if len(Robin) == 5:
        m = 0
        x = 0
        for i in Robin.keys():
            if Robin[i] > m:
                m = Robin[i]
                x = i
        del Robin[x]
    if number not in Robin:
        Robin[number] = 1
    #print sorted(Robin.keys()), rScore

x = 0
trails = 0
ex = 0

while True:
    Larry = dict()
    Robin = dict()
    lScore = 0
    rScore = 0
    for i in xrange(50):
        number = randint(1, 10)
        LarryPlays(number)
        RobinPlays(number)
    x += abs(lScore - rScore)
    trails += 1
    ex = x / float(trails)
    if trails % 10000 == 0:
        print trails, ex


#no ranking in suits!
#http://www.pagat.com/vying/pokerrank.html

cards = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
straights = [set([i, i+1, i+2, i+3, i+4]) for i in range(2, 11)]

def findDuplicates(v, numOfDup):
    dups = [0] * 15
    for value in v:
        dups[value] += 1
    ret = []
    for i in range(15):
        if dups[i]==numOfDup:
            ret.append(i)
    return sorted(ret)[::-1]
    
def checkFlush(s):
    return len(set(s))==1

def checkStraight(v):
    try:
        ret = straights.index(set(v)) + 6
    except:
        ret = -1
    return ret
    
def evalHand(h):
    score = 0
    v = sorted([cards.index(card[0]) for card in h])[::-1]
    s = [card[1] for card in h]
    twos = sorted(findDuplicates(v, 2))[::-1]
    threes = findDuplicates(v, 3)
    fours = findDuplicates(v, 4)
    flush = checkFlush(s)
    straight = checkStraight(v)
    if straight != -1:
        if flush:        #if it is straight flush
            score += (10**18) * straight
        else:            #if it is straight
            score += (10**16) * straight
    else:
        if flush:        #if it is flush
            score += (10**12)
        else:            #if neither
            if len(fours) > 0:           #four of a kind
                score += (10**14) * fours[0]
            else:
                if len(threes) > 0:
                    if len(twos) > 0:    #full house
                        score += (10**8) * (threes[0] * 100 + twos[0])
                    else:
                        score += (10**6) * threes[0] #three of a kind
                else:
                    if len(twos) > 1:    #two pairs
                        score += (10**2) * (twos[0] * 100 + twos[1])
                    elif len(twos) > 0:  #one pair
                        score += twos[0]
    return score
            

def compareHands(h1, h2):
    return [evalHand(h1), evalHand(h2)]
    

ans = 0
games = open('054.txt', 'r').read().split('\r\n')[:-1]
for game in games:
    k = game.split(' ')
    p1 = k[0:5]
    p2 = k[5:10]
    compare = compareHands(p1, p2)
    if compare[0] == compare[1]:
        v1 = sorted([cards.index(card[0]) for card in p1])[::-1]
        v2 = sorted([cards.index(card[0]) for card in p2])[::-1]
        for i in range(5):
            if v1[i] > v2[i]:
                ans +=1
                break
            elif v1[i] < v2[i]:
                break
            else:
                continue
    elif compare[0] > compare[1]:
        ans += 1
        
print ans

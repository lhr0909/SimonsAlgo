from random import randint

p = dict()
for i in xrange(40):
    p[i] = 0

die = 4
n = 100000 #number of simulations

#get the CH and CC cards ready
ch = []
cc = []
for i in xrange(16):
    tch = randint(1, 16)
    tcc = randint(1, 16)
    while tch in ch:
        tch = randint(1, 16)
    while tcc in cc:
        tcc = randint(1, 16)
    ch.append(tch)
    cc.append(tcc)

x = 0
for i in xrange(n):
    #make a move
    dice = randint(1, die) + randint(1, die)
    x = (x + dice) % 40
    if x == 2 or x == 17 or x == 33: #CC's
        if cc[0] == 1: #advance to GO
            x = 0
        elif cc[0] == 2: #go to JAIL
            x = 10
        cc = cc[1:] + [cc[0]] #put the top card to the bottom
    elif x == 7 or x == 22 or x == 36: #CH's
        if ch[0] == 1: #advance to GO
            x = 0
        elif ch[0] == 2: #go to JAIL
            x = 10
        elif ch[0] == 3: #go to C1
            x = 11
        elif ch[0] == 4: #go to E3
            x = 24
        elif ch[0] == 5: #go to H2
            x = 39
        elif ch[0] == 6: #go to R1
            x = 5
        elif ch[0] == 7 or ch[0] == 8: #go to next R
            if x == 7: #CH1 -> R2
                x = 15
            elif x == 22: #CH2 -> R3
                x = 25
            elif x == 36: #CH3 -> R1
                x = 5
        elif ch[0] == 9: #go to next U
            if x == 7: #CH1 -> U1
                x = 12
            elif x == 22: #CH2 -> U2
                x = 28
            elif x == 36: #CH3 -> U1
                x = 12
        elif ch[0] == 10: #go back 3 squares
            x = x - 3
            #I did not implement the possibility that CH3 might go back to CC3
            #and draw another CC card.
        ch = ch[1:] + [ch[0]] #put the top card to the bottom
    elif x == 30: #G2J
        x = 10
    p[x] += 1

ans = ""
max3 = sorted(p.values())[-3:]
max3.reverse()
for item in max3:
    for i in xrange(40):
        if p[i] == item:
            ans += "%02d" % i
print ans
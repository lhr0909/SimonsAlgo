from random import randint

def D4():
    return randint(1, 4)

def D6():
    return randint(1, 6)

total = 0
win = 0

while True:
    Peter = 0
    for i in xrange(9):
        Peter += D4()
    Colin = 0
    for i in xrange(6):
        Colin += D6()
    if Peter > Colin:
        win += 1
    total += 1
    if total % 1000000 == 0:
        print win, total, "%.10f" % (win / float(total))

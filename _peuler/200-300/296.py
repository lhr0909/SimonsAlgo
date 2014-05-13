##10 - 2 - 0.065s
##100 - 376 - 0.602s
##1000 - 61339 - 1min 18s
#
#import Maple
#
#maple = Maple.Maple()
#
#Maple.openNumTheory(maple)
#
#n = 100000
#count = 0
#
#for AB in xrange(1, n / 2 + 1):
#    for BC in xrange(1, AB + 1):
#        ta = AB * BC
#        d = Maple.divisors(maple, ta) #find divisors using maple
#        for divisor in d:
#            AC = divisor - BC
#            #check the validity of AC
#            if AC >= BC and AC <= AB and divisor > AB and divisor + AB <= n:
#                count += 1
#                print "%d-%d-%d ---- %d" % (BC, AC, AB, count)
#print count

def checkBE(BC, AC, AB):
    ta = AB * BC
    tb = AC + BC
    if ta % tb == 0:
        return ta / tb
    else:
        return False

#10 - 2 - 0.018s
#100 - 376 - 0.041s
#1000 - 61339 - 6.809s

n = 100
count = 0

for BC in xrange(1, n / 3 + 1):
    for AC in xrange(BC, n / 2 + 1):
        AB = AC
        while AB < BC + AC and BC + AC + AB <= n:
            BE = checkBE(BC, AC, AB)
            if BE:
                count += 1
                print "%d-%d-%d: %d ---- %d" % (BC, AC, AB, BE, count)
            AB += 1
print count

#for AB in xrange(1, n / 2+1):
#    for AC in xrange(AB / 2, AB + 1):
#        for BC in xrange(AC, 0, -1):
#            if BC + AC <= AB:
#                break
#            else:
#                if BC + AC + AB <= n:
#                    BE = checkBE(BC, AC, AB)
#                    if BE:
#                        count += 1
#                        print "%d-%d-%d: %d ---- %d" % (BC, AC, AB, BE, count)
#print count

##remember to delete maple, just to terminate it
#del maple
#include <stdio.h>
/*
//use law of consines to find out the angle measures of A, B, and C.
//and according to a theorem of Tangent Chord Angle, 
//we can find out the measure of acute angle mCB equals to the measure of angle CAB.
//and then we can draw a line perpendicular to n through C
//and we use Pythagorean theorem to find measure of BE. BINGO!
//appreciated my high school math... Should have learned it better.

//Special case: if BC = AC, just need to check if AB is even.

//Serious precision problem

#include <math.h>

long checkBE(long BC, long AC, long AB)
{
    double Pi = 4 * atan(1);
    double rightAngle = Pi / 2.0;
    double cosC, cosA;
    double mPCB, mACB, mKCB, mKCE;
    double CK, KE, KB, BE;
    cosC = (BC*BC + AC*AC - AB*AB) / ((double) 2*BC*AC);
    cosA = (AC*AC + AB*AB - BC*BC) / ((double) 2*AC*AB);
    mACB = acos(cosC);
    mPCB = acos(cosA);
    mKCB = rightAngle - mPCB;
    mKCE = mKCB - (mACB / 2.0);
    CK = BC * cos(mKCB);
    KE = CK * tan(mKCE);
    KB = sqrt(BC*BC - CK*CK);
    BE = KB - KE;
    if (BE == (long) BE) //if BE is integral
    {
        return ((long) BE);
    }
    else
    {
        return 0;
    }
}
*/

/*
Python Stuff
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
*/

long checkBE(long BC, long AC, long AB)
{
    long long tempA = AB * BC;
    long tempB = AC + BC;
    if (tempA % tempB == 0)
        return tempA / tempB;
    else
        return 0;
}

//10 - 2 - 0.001s
//100 - 376 - 0.010s
//1000 - 61339 - 3 secs
//10000 - 8740638 - 10 mins
//100000 - ?????????? - probably 12 hrs?

long gcd(long a, long b)
{
    long t;
    while (b != 0)
    {
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int main(int argc, char **argv)
{
    long BC;
    long AC;
    long AB;
    long BE;
    long temp;
    long g;
    long k;
    long long count = 0;
    long n = 100000;
    
    for (BC = 1; BC <= n / 3; BC++)
    {
        if (BC % 1000 == 0)
        {
            printf("%ld %lld\n", BC, count);
        }
        for (AC = BC; AC <= n / 2; AC++)
        {
            //count += ();
            temp = AC + BC;
            g = gcd(BC, temp);
            k = temp / g;
            if (AC % k == 0)
            {
                AB = k * (AC / k);
            }
            else
            {
                AB = k * ((AC / k) + 1);
            }
            while ((AB < BC + AC) && (BC + AC + AB <= n))
            {
                //BE = AB * BC / temp;
                count++;
                //printf("%ld-%ld-%ld: %ld ---- %lld\n", BC, AC, AB, BE, count);
                AB += k;
            }
        }
    }
    printf("%lld\n", count);
    return 0;
}

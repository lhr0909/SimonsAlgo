//related problem: 028.py
//another large prime problem. used C instead

#include <stdio.h>
#include <math.h>

int isPrime(long n)
{
    long i;
    if (n < 2)
    {
        return 0;
    }
    for (i = 2; i <= (int) sqrt(n); i++)
    {
        if (n % i==0)
        {
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    int d[] = {3, 3, 2, 2};
    
    int sides = 3;
    
    //initially is 1, 3, 5, 7, 9, so it has a ratio 3/5 = 0.6
    float numPrimes = 3.0;
    float numTotal = 5.0;
    float ratio = numPrimes / numTotal;
    
    int i;
    
    while (ratio > 0.1)
    {
        for (i = 0; i < 4; i++)
        {
            d[i] = d[i] + 2;
        }
        sides = sides + 2;
        
        if (isPrime(d[0]*d[0])==1)
        {
            numPrimes = numPrimes + 1.0;
        }
        if (isPrime(d[1]*d[1] - 2 * (d[1] / 2))==1)
        {
            numPrimes = numPrimes + 1.0;
        }
        if (isPrime(d[2]*d[2] + 1)==1)
        {
            numPrimes = numPrimes + 1.0;
        }
        if (isPrime((d[3]*d[3] + 1) - 2 * (d[3] / 2))==1)
        {
            numPrimes = numPrimes + 1.0;
        }
        //printf("\n");
        numTotal = numTotal + 4.0;
        ratio = numPrimes / numTotal;
        //printf("%f / %f = %f\n", numPrimes, numTotal, ratio);
    }
    printf("%d\n", sides);
    return 0;
}

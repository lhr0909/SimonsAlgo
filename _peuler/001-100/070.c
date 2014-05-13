//Euler's Totient Function
//Related Problem: 069

#include <stdio.h>
#include <string.h>

char prime[10000000];

void sieve(void)
{
    memset(prime, 0, sizeof(prime));
    long i, j;
    prime[0] = 1;
    prime[1] = 1;
    for (i = 2; i < 10000000; i++)
    {
        for (j = i*i; j < 10000000; j+=i)
        {
            if (j < 10000000)
            {
                prime[j] = 1;
            }
        }
    }
}

long long phi(long n)
{
    long i = 2;
    long k = n;
    long factors = 1;
    long factors_1 = 1;
    while (k != 1)
    {
        if (prime[i] == 0)
        {
            if (k % i == 0)
            {
                factors = factors * i;
                factors_1 = factors_1 * (i - 1);
                while (k % i == 0)
                {
                    k = k / i;
                }
            }
            else
            {
                i++;
            }
        }
        else
        {
            i++;
        }
    }
    return n * factors_1 / factors;
}

int isPermutation(long long x, long long y)
{
    long i[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    long j[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
    long long k;
    k = x;
    while (k > 0)
    {
        i[k % 10]++;
        k = k / 10;
    }
    k = y;
    while (k > 0)
    {
        j[k % 10]++;
        k = k / 10;
    }
    for (k = 0; k < 10; k++)
    {
        if (i[k] != j[k])
        {
            return 0;
        }
    }
    return 1;
}

int main(int argc, char **argv)
{
    long long n;
    long long m;
    double t;
    double minR = 999999.0;
    long long ans;
    sieve();
    printf("Finish making primes\n");
    for (n = 2; n < 10000000; n++)
    {
        m = phi(n);
        if (isPermutation(m, n))
        {
            t = (double) n / (double) m;
            if (t < minR)
            {
                ans = n;
                minR = t;
                printf("%lld %lld %g\n", n, m, t);
            }
        }
    }
    printf("%lld\n", ans);
    return 0;
}

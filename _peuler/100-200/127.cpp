#include <iostream>
#include <cstring>
using namespace std;

long primes[120000] = {0};
long rad[120000];
long pCount = 0;

void makePrimes()
{
    bool isP[120000];
    memset(isP, 1, sizeof(isP));
    isP[0] = false;
    isP[1] = false;
    for (long i = 2; i < 120000; i++)
    {
        if (isP[i])
        {
            primes[pCount] = i;
            pCount++;
            for (long j = i * i; j < 120000; j += i)
            {
                isP[j] = false;
            }
        }
    }
}

void makeRAD()
{
    for (long i = 0; i < 120000; i++) rad[i] = 1;
    long k;
    for (long i = 0; i < pCount; i++)
    {
        k = primes[i];
        for (long j = k; j < 120000; j += k)
        {
            rad[j] *= primes[i];
        }
    }
}

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

long abcHit()
{
    long ans = 0;
    makePrimes();
    makeRAD();
    for (long c = 3; c < 120000; c++)
    {
        for (long a = 1; a < (c + 1) / 2; a++)
        {
            long b = c - a;
            if ((gcd(a, b) == 1) && (gcd(b, c) == 1) && (gcd(a, c) == 1))
            {
                long radc = rad[a] * rad[b] * rad[c];
                if (radc < c)
                {
                    //it is an abc-hit
                    ans += c;
                    cout << a << " " << b << " " << c << " " << ans << endl;
                }
            }
        }
        
    }
    return ans;
}

int main()
{
    cout << abcHit() << endl;
    return 0;
}

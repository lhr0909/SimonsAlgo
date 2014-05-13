#include <iostream>
#include <cstdio>
using namespace std;

#ifndef for1
    #define for1(N, k) for (int N = 1; N <= k; N++)
#endif

int main()
{
    long Peter[36] = {0};
    long Colin[36] = {0};
    long long p = 262144;
    long long c = 46656;
    long long n = p * c;
	long long x = 0;
	cout << n << endl;
    for1(d1, 4)
        for1(d2, 4)
            for1(d3, 4)
                for1(d4, 4)
                    for1(d5, 4)
                        for1(d6, 4)
                            for1(d7, 4)
                                for1(d8, 4)
                                    for1(d9, 4)
                                        Peter[d1+d2+d3+d4+d5+d6+d7+d8+d9-1]++;
    for1(d1, 6)
        for1(d2, 6)
            for1(d3, 6)
                for1(d4, 6)
                    for1(d5, 6)
                        for1(d6, 6)
                            Colin[d1+d2+d3+d4+d5+d6-1]++;

    for (int i = 9; i <= 36; i++)
    {
        for (int j = 6; j < i; j++)
        {
            x += Peter[i-1] * Colin[j-1];
        }
    }

    long double ans = x / (long double) n;
    cout.setf(ios::fixed);
    cout.precision(7);
    cout << ans << endl;
    return 0;
}

#include <iostream>
#include <cstdio>
using namespace std;

int gcd(int a, int b)
{
    int t;
    while (b != 0)
    {
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}

int lcm(int a, int b)
{
    return (a * b) / gcd(a, b);
}

int main()
{
    int n = 1;
    int s = 0;
    while (s <= 1000)
    {
        s = 0;
        int x = n + 1;
        while (x <= 2 * n)
        {
            int y = lcm(n, x);
            if ((x * y) / (x + y) == n)
            {
                //printf("1/%d + 1/%d = 1/%d", x, y, n);
                s++;
            }
            x++;
        }
        cout << n << " " << s << endl;
        n++;
    }
    cout << n - 1 << endl;
    return 0;
}

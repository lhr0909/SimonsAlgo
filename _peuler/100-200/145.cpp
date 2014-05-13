#include <iostream>
using namespace std;

bool Reversible(long n)
{
    int digit[10] = {0};
    int nd = 0;
    int k = n;
    while (k != 0)
    {
        digit[nd] = k % 10;
        k /= 10;
        nd++;
    }
    if (!digit[0]) return false; //no leading 0's
    int j = 1;
    k = 0;
    for (int i = nd - 1; i >= 0; i--)
    {
        k += digit[i] * j;
        j *= 10;
    }
    k = n + k;
    while (k != 0)
    {
        if ((k % 10) % 2 == 0) return false; //if a even digit is found
        k /= 10;
    }
    return true;
}

int main()
{
    long count = 0;
    //count seems not to grow after 100 million... truncated it
    //numerical analysis on the forum...
    for (long i = 11; i < 90000000; i++)
    {
        if (Reversible(i)) count++;
    }
    cout << count << endl;
    return 0;
}

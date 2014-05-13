#include <iostream>
#include <map>

using namespace std;

map<long long, long long> sd;
map<long long, long long>::iterator iter;

long long mod(long long a, long long b)
{
    long long temp = a % b;
    if (temp < 0)
    {
        temp = b + temp;
    }
    return temp;
}

long long s(long long k)
{
    iter = sd.find(k);
    if (iter != sd.end())
    {
        return iter->second;
    }
    else
    {
        if (k <= 55)
        {
            sd[k] = mod((100003 - 200003 * k + 300007 * k * k * k), 1000000) - 500000;
        }
        else
        {
            sd[k] = mod((s(k - 24) + s(k - 55) - 1000000), 1000000) - 500000;
        }
        return sd[k];
    }
}

int main()
{
    cout << "Caching numbers... " << endl;
    for (long i = 1; i <= 4000000; i++)
    {
        s(i);
    }
    cout << "Finished." << endl;
    return 0;
}

#include <iostream>
#include <deque>
#include <map>
#include <cmath>
using namespace std;

struct triangle
{
    long long a;
    long long b;
    long long h;
};

int main()
{
    deque<triangle> q;
    map<long long, triangle> d;
    triangle t, s;
    long long x;
    long long count = 0;
    long long k;
    t.a = 3;
    t.b = 4;
    t.h = 5;
    q.push_back(t);
    while (!q.empty())
    {
        t = q.front();
        q.pop_front();
        k = t.a + t.b + t.h;
        if (k < 100000000)
        {
            if (t.a > t.b)
            {
                x = t.a - t.b;
            }
            else
            {
                x = t.b - t.a;
            }
            if (t.h % x == 0)
            {
                cout << t.a << " " << t.b << " " << t.h << " " << count << endl;
                count += (100000000 / k);
            }
            d[t.a + t.b + t.h] = t;
            s.a = t.a-2*t.b+2*t.h;
            s.b = 2*t.a-t.b+2*t.h;
            s.h = 2*t.a-2*t.b+3*t.h;
            q.push_back(s);
            s.a = t.a+2*t.b+2*t.h;
            s.b = 2*t.a+t.b+2*t.h;
            s.h = 2*t.a+2*t.b+3*t.h;
            q.push_back(s);
            s.a = (-1*t.a)+2*t.b+2*t.h;
            s.b = (-2*t.a)+t.b+2*t.h;
            s.h = (-2*t.a)+2*t.b+3*t.h;
            q.push_back(s);
        }
    }
    cout << count << endl;
    return 0;
}

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<map>

using namespace std;

map<long, long long> coinCache;

long long coin(long n) {
    map<long, long long>::iterator it;
    it = coinCache.find(n);
    if (it != coinCache.end()) {
        return coinCache[n];
    } else {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            coinCache[n] = coin(n/2) + coin(n/3) + coin(n/4);
            if (n > coinCache[n]) {
                coinCache[n] = n;
            }
            return coinCache[n];
        }
    }
}

int main(void)
{
    coinCache[0] = 0;
    coinCache[1] = 1;
    long n;
    while (scanf("%ld", &n) == 1) {
        cout << coin(n) << endl;
    }
    return 0;
}

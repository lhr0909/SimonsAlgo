#include<iostream>
#include<cstdlib>

using namespace std;

int compare (const void *p1, const void *p2) {
    return (*(int*)p2 - *(int*)p1);
}

int main(void)
{
    int n = 0;
    cin >> n;
    while (n >= 0) {
        int candy[n];
        long sum = 0;
        for (int i = 0; i < n; i++) {
            cin >> candy[i];
            sum += candy[i];
        }
        if (sum % n != 0) {
            cout << -1 << endl;
        } else {
            long offset = 0;
            long avg = sum / n;
            for (int i = 0; i < n; i++) {
                if (avg > candy[i]) {
                    offset += avg - candy[i];
                }
            }
            cout << offset << endl;
        }
        cin >> n;
    }
    return 0;
}


#include<iostream>
#include<cstdlib>

using namespace std;

int main(void)
{
    int t;
    long long N;
    long long sum;
    long long candy;
    cin >> t;
    for (int tt = 0; tt < t; tt++) {
        cin >> N;
        sum = 0;
        for (long long i = 0; i < N; i++) {
            cin >> candy;
            sum += candy % N;
        }
        if (sum % N == 0) {
            cout << "YES";
        } else {
            cout << "NO";
        }
        cout << endl;
    }
    return 0;
}

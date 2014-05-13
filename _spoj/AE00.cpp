#include<iostream>
#include<cstdlib>

using namespace std;

int main(void)
{
    int N;
    long sum = 0;
    cin >> N;
    for (int i = 1; i <= N;i++) {
        for (int j = i; j <= N; j++) {
            if (i * j <= N) {
                sum++;
            }
        }
    }
    cout << sum;
    return 0;
}

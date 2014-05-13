#include<iostream>
#include<cstdlib>

using namespace std;

int compare (const void *p1, const void *p2) {
    return (*(int*)p2 - *(int*)p1);
}

int main(void)
{
    int t;
    int N;
    int hotGuys[1000], hotGirls[1000];
    int sum;
    cin >> t;
    for (int tt = 0; tt < t; tt++) {
        cin >> N;
        for (int i = 0; i < N; i++) {
            cin >> hotGuys[i];
        }
        for (int i = 0; i < N; i++) {
            cin >> hotGirls[i];
        }
        qsort(hotGuys, N, sizeof(int), compare);
        qsort(hotGirls, N, sizeof(int), compare);
        sum = 0;
        for (int i = 0; i < N; i++) {
            sum += hotGuys[i] * hotGirls[i];
        }
        cout << sum << endl;
    }
    return 0;
}

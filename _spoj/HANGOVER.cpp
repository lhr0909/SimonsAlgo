#include<iostream>

using namespace std;

int main(void) {
    double c;
    cin >> c;
    while (c > 0.00001) {
        int i = 0;
        double length = 0;
        while (length < c) {
            i++;
            length += 1 / (double)(i+1);
        }
        cout << i << " card(s)" << endl;
        cin >> c;
    }
    return 0;
}

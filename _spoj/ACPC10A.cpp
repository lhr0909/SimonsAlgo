#include<iostream>
#include<cstdlib>

using namespace std;

int main(void)
{
    int a = 1;
    int b = 1;
    int c = 1;
    cin >> a >> b >> c;
    while ((a != 0) || (b != 0) || (c != 0)) {
        if ((c - b == b - a) && (c - b != 0)) {
            cout << "AP " << c + (c - b) << endl;
        } else {
            cout << "GP " << c * (c / b) << endl;
        }
        cin >> a >> b >> c;
    }
    return 0;
}

#include<iostream>

using namespace std;

int main(void) {
    string s;
    int count[5000];
    
    cin >> s;
    while (s.compare("0") != 0) {
        int len = s.length();
        count[0] = 1;
        for (int i = 1; i < len; i++) {
            string currentDigit = s.substr(i, 1);
            string current2Digit = s.substr(i - 1, 2);
            int cDigitNum = currentDigit[0] - '0';
            int c2DigitNum = (current2Digit[0] - '0') * 10 + (current2Digit[1] - '0');
            int c = 0;
            if (cDigitNum > 0) {
                if (c2DigitNum <= 26) {
                    if (i - 2 > 0) {
                        c = count[i - 2] + count[i - 1] + 2;
                    } else {
                        c = count[i - 1] + 1;
                    }
                } else {
                    c = count[i - 1] + 1;
                }
            } else {
                if (c2DigitNum <= 26) {
                    c = count[i - 2] + 1;
                }
            }
            count[i] = c;
        }
        cout << count[len - 1] << endl;
        cin >> s;
    }
    return 0;
}
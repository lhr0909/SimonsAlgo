#include<iostream>
#include<cstdlib>

using namespace std;

template <typename T>
T modpow(T base, T exp, T modulus) {
  base %= modulus;
  T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}

int main(void)
{
    int t;
    cin >> t;
    for (int tt = 0; tt < t; tt++) {
        int a, b;
        cin >> a >> b;
        int digit = modpow(a, b, 10);
        cout << digit << endl;
    }
    return 0;
}


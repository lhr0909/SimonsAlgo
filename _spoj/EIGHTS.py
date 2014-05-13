#Used power mod and found the pattern. Super easy problem

'''
#include<iostream>
#include<cstdlib>

using namespace std;

//test code
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
        int n;
        cin >> n;
        long long i = 1;
        int count = 0;
        while (count < n) {
            if (modpow(i, (long long) 3, (long long) 1000) == 888) {
                cout << i << endl;
                count++;
            }
            i++;
        }
    }
    return 0;
}
'''

number_list = ["192", "442", "692", "942"]

t = int(raw_input())
for tt in xrange(t):
    n = int(raw_input())
    quotient = (n - 1) / 4
    # minus 1 for matching on the number_list
    remainder = n % 4 - 1
    print (str(quotient) if quotient > 0 else "") + number_list[remainder]
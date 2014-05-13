// http://oeis.org/A000330

#include <iostream>

using namespace std;
int main() {
	int n = -1;
	long ans = 0;
	while (n != 0) {
		cin >> n;
		if (n != 0) {
			ans = (2*n*n*n + 3*n*n + n) / 6;
			cout << ans << endl;			
		}

	}
	return 0;
}

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(void) {
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int testCase;
    long double fixedRate = 2;
    long double currentTime, minTime, farmTime;
    fin >> testCase;
    cout << testCase << endl;
    for (int testCaseI = 1; testCaseI <= testCase; testCaseI++) {
        long double C, F, X;
        fin >> C >> F >> X;

        minTime = X / fixedRate;
        currentTime = X / fixedRate;
        farmTime = 0;
        long farmCount = 1;
        while (currentTime <= minTime) {
            farmTime += C / (fixedRate + F * (farmCount - 1));
            currentTime = farmTime + X / (fixedRate + F * farmCount);
            if (currentTime < minTime) {
                minTime = currentTime;
            }
            farmCount++;
        }
        cout.precision(7);
        fout.precision(7);
        cout << fixed << minTime << endl;
        fout << "Case #" << testCaseI << ": " << fixed << minTime << endl;
    }
    fout.close();
    return 0;
}


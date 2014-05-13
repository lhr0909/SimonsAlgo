#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int sortLargeToSmall (const void *p1, const void *p2) {
    if (*(float*)p2 < *(float*)p1) return -1;
    if (*(float*)p2 == *(float*)p1) return 0;
    if (*(float*)p2 > *(float*)p1) return 1;
}

int sortSmallToLarge (const void *p1, const void *p2) {
    if (*(float*)p1 < *(float*)p2) return -1;
    if (*(float*)p1 == *(float*)p2) return 0;
    if (*(float*)p1 > *(float*)p2) return 1;
}

int main(void) {
    ifstream fin("D-large.in");
    ofstream fout("D-large.out");
    int testCase;
    fin >> testCase;
    float naomi[1000], ken[1000];
    cout << testCase << endl;
    for (int testCaseI = 1; testCaseI <= testCase; testCaseI++) {
        int N;
        fin >> N;
        for (int i = 0; i < N; i++) {
            fin >> naomi[i];
        }
        for (int i = 0; i < N; i++) {
            fin >> ken[i];
        }
        //sort both first
        qsort(naomi, N, sizeof(float), sortSmallToLarge);
        qsort(ken, N, sizeof(float), sortSmallToLarge);

/*
        for (int i = 0; i < N; i++) {
            cout << naomi[i] << " ";
        }
        cout << endl;
*/

        fout << "Case #" << testCaseI << ": ";

        int deceitfulWarWins = 0;

        for (int i = 0; i < N; i++) {
            if (naomi[i] < ken[i]) {
                //bluff him to use the top stuff
                float temp;
                for (int j = N-1; j > i; j--) {
                    temp = ken[j];
                    if (j == N-1) {
                        ken[j] = ken[i];
                        ken[i] = temp;
                    } else {
                        ken[j] = ken[j+1];
                        ken[j+1] = temp;
                    }
                }
            }
            if (naomi[i] > ken[i]) {
                deceitfulWarWins++;
            }
        }
/*
        for (int i = 0; i < N; i++) {
            cout << ken[i] << " ";
        }
        cout << endl;
*/
        fout << deceitfulWarWins << " ";



        int warWins = 0;
        //sort both first
        qsort(naomi, N, sizeof(float), sortLargeToSmall);
        qsort(ken, N, sizeof(float), sortLargeToSmall);

        for (int i = 0; i < N; i++) {
            if (naomi[i] > ken[i]) {
                //feed her the bottom crap
                float temp;
                for (int j = N-1; j > i; j--) {
                    temp = ken[j];
                    if (j == N-1) {
                        ken[j] = ken[i];
                        ken[i] = temp;
                    } else {
                        ken[j] = ken[j+1];
                        ken[j+1] = temp;
                    }
                }
            }
            if (naomi[i] > ken[i]) {
                warWins++;
            }
        }
/*
        for (int i = 0; i < N; i++) {
            cout << naomi[i] << " ";
        }
        cout << endl;
        for (int i = 0; i < N; i++) {
            cout << ken[i] << " ";
        }
        cout << endl << "result: ";
        cout << deceitfulWarWins << " " << warWins << endl << endl;
*/
        fout << warWins << endl;
    }
    fout.close();
    return 0;
}


#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(void) {
    ifstream fin("D-tiny.in");
    ofstream fout("D-tiny.out");
    int testCase;
    fin >> testCase;
    cout << testCase << endl;
    for (int testCaseI = 1; testCaseI <= testCase; testCaseI++) {
        int numKeys, numChests;
        cout << "Case #" << testCaseI << ": " << endl;
        fin >> numKeys >> numChests;
        vector<int> keys;
        cout << "You have these keys to start with: ";
        for (int i = 0; i < numKeys; i++) {
            int key;
            fin >> key;
            cout << key << " ";
            keys.push_back(key);
        }
        cout << endl;
        int keyChestNeeds[numChests];
        int numKeysInChest[numChests];
        int keysInChest[numChests][numChests];
        for (int i = 0; i < numChests; i++) {
            fin >> keyChestNeeds[i] >> numKeysInChest[i];
            cout << "Chest " << i+1 << " needs key #" << keyChestNeeds[i] << " to open, and has " << numKeysInChest[i] << " keys: ";
            for (int j = 0; j < numKeysInChest[i]; j++) {
                fin >> keysInChest[i][j];
                cout << keysInChest[i][j] << " ";
            }
            cout << endl;
        }
    }
    fout.close();
    return 0;
}

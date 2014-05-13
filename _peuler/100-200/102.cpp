#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

//let origin be point O
//let (OA . OB) / (|OA| * |OB|) = cosA
//let (OC . OB) / (|OC| * |OB|) = cosB
//let (OA . OC) / (|OA| * |OC|) = cosC

//calculate the acrcos of cosA, cosB, cosC, sum them up.
//if it is equal to 2*Pi, then origin is in the triangle.

//It is also cool just to check the areas using Heron's formula.

bool isIn(int x1, int y1, int x2, int y2, int x3, int y3)
{
    double OAdOB = x1*x2 + y1*y2;
    double OCdOB = x3*x2 + y3*y2;
    double OAdOC = x1*x3 + y1*y3;
    double OAtOB = sqrt(x1*x1 + y1*y1) * sqrt(x2*x2 + y2*y2);
    double OCtOB = sqrt(x3*x3 + y3*y3) * sqrt(x2*x2 + y2*y2);
    double OAtOC = sqrt(x1*x1 + y1*y1) * sqrt(x3*x3 + y3*y3);
    double cosA = OAdOB / OAtOB;
    double cosB = OCdOB / OCtOB;
    double cosC = OAdOC / OAtOC;
    double A = acos(cosA);
    double B = acos(cosB);
    double C = acos(cosC);
    double total = A + B + C;
    double Pi2 = 2 * 3.141592653589793238;
    //cout << total <<endl;
    return (abs(total - Pi2) < 0.00001);
}

int main()
{
    freopen("102.txt", "r", stdin);
    int count = 0;
    double l1, l2, l3;
    
    int x1, y1, x2, y2, x3, y3;
    for (int i = 0; i < 1000; i++)
    {
        cin >> x1;
        cin.get();
        cin >> y1;
        cin.get();
        cin >> x2;
        cin.get();
        cin >> y2;
        cin.get();
        cin >> x3;
        cin.get();
        cin >> y3;
        
        if (isIn(x1, y1, x2, y2, x3, y3))
        {
            count++;
        }
    }
    cout << count << endl;
    return 0;
}

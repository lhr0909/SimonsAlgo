#include <iostream>
#include <cstdio>
using namespace std;

//c[n][i][j][k] is the number of solutions for a (n+1) digit number that
//no three consecutive digits is greater than 9 and ends in (i)(j)(k).

//so for c[2][i][j][k], I looped through to find the total count.
//and then I basically dynamic programmed the rest, and build it up.
//The main loop is quite easy to understand.
//and the sum up all the c[19][i][j][k] values.

long long c[20][10][10][10] = {0};

long long ans = 0;

int main()
{
    //freopen("out.txt", "w", stdout);
    for (int i = 1; i < 10; i++)
    {
        for (int j = 0; j < 10 - i; j++)
        {
            for (int k = 0; k < 10 - j - i; k++)
            {
                //cout << i << " " << j << " " << k << endl;
                c[2][k][j][i] = 1;
                /*
                //test loop
                for (int m = 0; m < 10 - k - j; m++)
                {
                    ans++;
                }
                */
            }
        }
    }
    //cout << ans << endl;
    
    for (int n = 3; n < 20; n++)
    {
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < 10 - i; j++)
            {
                for (int k = 0; k < 10 - i - j; k++)
                {
                    for (int p = 0; p < 10 - j - k; p++)
                    {
                        c[n][i][j][k] += c[n-1][j][k][p];
                    }
                }
            }
        }
    }
    
    ans = 0;
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            for (int k = 0; k < 10; k++)
            {
                ans += c[19][i][j][k];
            }
        }
    }
    cout << ans << endl;
    //fclose(stdout);                   
    return 0;
}

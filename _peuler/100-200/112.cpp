#include <iostream>
using namespace std;

bool isBouncy(long n)
{
    if (n < 100) return false;
    long k = n;
    int currentDigit = k % 10;
    int lastDigit = currentDigit;
    int state;
    k = k / 10;
    currentDigit = k % 10;
    k = k / 10;
    if (currentDigit == lastDigit)
    {
        state = 0;
    }
    else 
    {
        if (currentDigit < lastDigit)
        {
            state = -1;
        }
        else
        {
            state = 1;
        }
    }
    while (k != 0)
    {
        lastDigit = currentDigit;
        currentDigit = k % 10;
        k = k / 10;
        if (currentDigit == lastDigit)
        {
            continue;
        }
        else
        {
            if (currentDigit < lastDigit)
            {
                switch (state)
                {
                    case 0:
                        state = -1;
                        break;
                    case 1:
                        return true;
                }
            }
            else
            {
                switch (state)
                {
                    case 0:
                        state = 1;
                        break;
                    case -1:
                        return true;
                }
            }
        }
    }
    return false;
}

int main()
{
    long count = 0;
    long total = 0;
    double percentage = 1.0;
    long i = 1;
    while (percentage != 0.99)
    {
        if (isBouncy(i))
        {
            count++;
        }
        total++;
        percentage = count / (double) total;
        i++;
    }
    cout << total << endl;
    return 0;
}

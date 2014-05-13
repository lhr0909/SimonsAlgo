//http://www.research.att.com/~njas/sequence/A143715
//http://www.research.att.com/~njas/sequence/A143714

//used the formula in A143714, and get the partial sum to get A143715

//I actually had a code for calculating that in O(n^3), but I deleted it...
//I found the sequence with that code, and typed it in OEIS...

#include <stdio.h>
#include <math.h>

int main(int argc, char **argv)
{
    int m = 1;
    int count = 0;
    int a, b;
    double s;
    while (count < 1000000)
    {
        for (a = 1; a <= m; a++)
        {
            for (b = a; b <= m; b++)
            {
                s = sqrt((a+b)*(a+b) + m*m);
                if (s == (int) s)
                {
                    count++;
                }
            }
        }
        printf("%d %d\n", m, count);
        m++;
    }
    return 0;
}

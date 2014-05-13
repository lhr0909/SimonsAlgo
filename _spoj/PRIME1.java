package spoj;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        while(true) {
            Scanner in = new Scanner(System.in);

            int n = in.nextInt();

            for (int i = 0; i < n; i++) {
                long x = in.nextInt();
                long y = in.nextInt();
                long temp = x - 1;
                temp = nextPrime(temp);
                while (temp <= y) {
                    System.out.println(temp);
                    temp = nextPrime(temp);
                }
                if (i < n - 1) System.out.println();
            }
            String line = in.next();
            if (line == null) break;
        }
    }

    private static long nextPrime(long n) {
        long i = n + 1;
        while (!isPrime(i)) i++;
        return i;
    }

    private static boolean isPrime(long n) {
        if (n < 2) {
            return false;
        } else if ((n == 2) || (n == 3)) {
            return true;
        } else if ((n > 3) && (n % 2 == 0)) {
            return false;
        } else return millerRabin(n);
    }

    private static boolean millerRabin(long n) {

        //first, factor (n - 1) as (2^s * d)
        int s = 0;
        long d = n - 1;
        while (d % 2 == 1) { s++; d /= 2; }

        int[] A;
        if (n < 1373653) {
            A = new int[2];
            A[0] = 2;
            A[1] = 3;
        } else if (n < 9080191) {
            A = new int[2];
            A[0] = 31;
            A[1] = 73;
        } else {
            A = new int[3];
            A[0] = 2;
            A[1] = 7;
            A[2] = 61;
        }
        /*
        }else if (n < 4759123141) {
            int[] A = {2, 7, 61};
        } else if (n < 2152302898747) {
            int[] A = {2, 3, 5, 7, 11};
        } else if (n < 3474749660383) {
            int[] A = {2, 3, 5, 7, 11, 13};
        } else { // if n < 341550071728321
            int[] A = {2, 3, 5, 7, 11, 13, 17};
        }*/

        for (int i = 0; i < A.length; i++) {
            int a = A[i];
            boolean flag = false;
            long x = powerMod(a, d, n);
            if ((x == 1) || (x == n - 1)) {
                continue;
            }
            for (int r = 0; r < s - 1; r++) {
                x = powerMod(x, 2, n);
                if (x == 1) return false;
                if (x == n - 1) { flag = true; break; }
            }
            if (!flag) return false;
        }
        return true;
    }

//    private static long powerMod(long a, long b, long m) {
//        long  tempo;
//        if (b ==0 ){
//            tempo =  1;
//        }//if
//        else  if (b == 1) tempo = a;
//        else { long temp = powerMod(a, b / 2, m);
//            if (b%2 == 0)
//                tempo = (temp*temp)%m;
//            else
//                tempo = ((temp*temp)%m)*a%m;
//        }
//        return tempo;
//    }


    private static long powerMod(long a, long b, long m) {
        a %= m;
        long result = 1;
        while (b > 0) {
            if (b % 2 == 1) result = (result * a) % m;
            a = (a * a) % m;
            b >>= 1;
        }
        return result;
    }
}

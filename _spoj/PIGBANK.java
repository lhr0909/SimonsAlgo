package spoj;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int caseCount = in.nextInt();

        for (int T = 0; T < caseCount; T++) {
            int E = in.nextInt();
            int F = in.nextInt();
            int N = in.nextInt();

            int[] P = new int[N];
            int[] W = new int[N];
            int[] c = new int[F-E+1];
            for (int i = 0; i < N; i++) {
                P[i] = in.nextInt();
                W[i] = in.nextInt();
            }

            for (int i = 1; i <= F-E; i++) {
                int minVal = Integer.MAX_VALUE;
                for (int j = 0; j < N; j++) {
                    if ((i - W[j] >= 0) && (c[i-W[j]] >= 0) && (c[i-W[j]] + P[j] < minVal)) {
                        minVal = c[i-W[j]] + P[j];
                    }
                }
                if (minVal == Integer.MAX_VALUE) {
                    c[i] = -1;
                } else {
                    c[i] = minVal;
                }
            }

            if (c[F-E] == -1) {
                System.out.println("This is impossible.");
            } else {
                System.out.println("The minimum amount of money in the piggy-bank is " + c[F-E] + ".");
            }
        }
    }
}

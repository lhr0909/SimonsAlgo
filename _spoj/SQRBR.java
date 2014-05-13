package spoj;

import java.util.Scanner;

// http://www.derekillchuk.com/2010/06/square-brackets-permutation/

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int caseCount = in.nextInt();
        int[] positions;
        int[][] c;

        for (int t = 0; t < caseCount; t++) {
            int n = in.nextInt();
            int K = in.nextInt();
            positions = new int[K];
            for (int i = 0; i < K; i++) {
                positions[i] = in.nextInt();
            }

            c = new int[2*n+1][n+1];
            c[0][0] = 1;

            for (int i = 1; i <= 2*n; i++) {
                for (int j = 0; j <= n; j++) {
                    int x = 0;
                    int y = 0;
                    if (j-1 >= 0)
                        x = c[i-1][j-1];
                    if (j+1 <= n) {
                        for (int k = 0; k < K; k++) {
                            if (positions[k] == i) {
                                y = 0;
                                break;
                            } else {
                                y = c[i-1][j+1];
                            }
                        }
                    }
                    c[i][j] = x + y;

                }
            }

            System.out.println(c[2*n][0]);
        }
    }
}

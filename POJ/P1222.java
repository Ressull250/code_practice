import java.util.Scanner;
import java.util.TreeMap;

public class P1222 {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[][] input = new int[6][8];

        for(int k=1; k<=n; k++){
            //输入
            for (int i=1; i<6; i++){
                for (int j=1; j<7; j++){
                    input[i][j] = scanner.nextInt();
                }
            }

            enumr(input, k);
        }
    }

    public static void enumr(int[][] input, int k){
        //枚举第一列
        for (int i=0; i<64; i++){
            int[][] out = new int[6][8];
            for (int j=0; j<6; j++){
                out[1][j+1] = getBit(i,j);
            }

            for (int m=2; m<6; m++){
                for (int j=1; j<7; j++){
                    out[m][j] = (out[m-2][j] + out[m-1][j-1] + out[m-1][j] + out[m-1][j+1] + input[m-1][j]) % 2;
                }
            }

            boolean conflict = false;
            for (int j=1; j<7; j++){
                if ((out[5][j] + out[4][j] + out[5][j-1] + out[5][j+1] + input[5][j]) % 2 != 0){
                    conflict = true;
                    break;
                }
            }
            if (conflict)
                continue;
            else{
                output(out,k);
                break;
            }
        }
    }


    public static int getBit(int i, int k){
        return ((i & (1<<k)) > 0) ? 1 : 0;
    }

    public static void output(int[][] input, int k){
        System.out.println("PUZZLE #"+k);
        for (int i=1; i<6; i++){
            for (int j=1; j<7; j++){
                System.out.print(input[i][j]);
                if (j != input[0].length){
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
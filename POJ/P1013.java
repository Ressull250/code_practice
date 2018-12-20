import java.util.Scanner;

public class P1013 {

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String[][] input = new String[3][3];

        while ((n--) > 0){
            for (int i=0; i<3; i++){
                for (int j=0; j<3; j++){
                    input[i][j] = scanner.next();
                }
            }

            char t = 'A';
            while (t <= 'L') {
                if (isFake(input ,t, true)) {
                    System.out.println(t+" is the counterfeit coin and it is heavy.");
                    break;
                }
                else if(isFake(input, t, false)){
                    System.out.println(t+" is the counterfeit coin and it is light.");
                    break;
                }

                t++;
            }
        }
    }

    //模拟t是假币是否矛盾
    public static boolean isFake(final String[][] input, char t, boolean isHeavy){

        for (int i=0; i<3; i++) {
            String[] strs = input[i];
            switch (strs[2].charAt(0)) {
                case 'e': {
                    if (strs[0].indexOf(t) >= 0 || strs[1].indexOf(t) >= 0)
                        return false;
                    break;
                }
                case 'u': {
                    if (isHeavy && strs[0].indexOf(t) != -1) {
                        continue;
                    } else if (!isHeavy && strs[1].indexOf(t) != -1) {
                        continue;
                    }
                    return false;
                }
                case 'd': {
                    if (isHeavy && strs[1].indexOf(t) != -1) {
                        continue;
                    } else if (!isHeavy && strs[0].indexOf(t) != -1) {
                        continue;
                    }
                    return false;
                }
            }
        }
        return true;
    }
}
import java.util.Arrays;

public class Q61 {
    public boolean isContinuous(int [] numbers) {
        if (numbers == null || numbers.length != 5) return false;

        int wildcards = 0;
        int small = 0;
        int big = numbers.length-1;
        Arrays.sort(numbers);
        for (int i=0; i<numbers.length; i++){
            if (numbers[i] == 0)
                wildcards++;
            else{
                small = i;
                break;
            }
        }

        if (numbers[big] - numbers[small] > 4){
            return false;
        }

        for (int i=small+1; i<numbers.length; i++){
            if (numbers[i] == numbers[i-1])
                return false;
            wildcards -= (numbers[i]-numbers[i-1]-1);
            if (wildcards<0)
                return false;
        }

        return true;
    }
}

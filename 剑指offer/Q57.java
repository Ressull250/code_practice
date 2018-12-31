import java.util.ArrayList;
public class Q57 {
    public ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {
        int l=0, r=array.length-1;
        int num1=0, num2=0;
        int min=Integer.MAX_VALUE;

        while (l < r){
            int t = array[l] + array[r];
            if (t == sum){
                if (array[l]*array[r]<min){
                    min=array[l]*array[r];
                    num1=array[l];
                    num2=array[r];
                }
                l++;
                r--;
            }else if (t > sum){
                r--;
            }else
                l++;
        }
        ArrayList<Integer> res = new ArrayList<>();
        if (min != Integer.MAX_VALUE){
            res.add(num1);
            res.add(num2);
        }
        return res;
    }
}
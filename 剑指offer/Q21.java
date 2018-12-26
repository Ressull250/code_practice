import java.util.ArrayList;
import java.util.List;

public class Q21 {

    //oj上要求相对位置不变
    public void reOrderArray(int [] array) {
        List<Integer> t = new ArrayList<>();
        for (int i=0; i<array.length; i++){
            if (isEven(array[i]))
                t.add(array[i]);
            else
                array[i-t.size()] = array[i];
        }
        for (int i=0; i<t.size(); i++){
            array[array.length-t.size()+i] = t.get(i);
        }
    }

    //书上的没有要求相对位置不变
    public void reOrderArrayWithChanges(int [] array) {

        int l=0, r=array.length-1;
        while (l<r){
            while (l<=r && !isEven(array[l]))
                l++;
            while (l<=r && isEven(array[r]))
                r--;
            if (l<r){
                int t = array[l];
                array[l] = array[r];
                array[r] = t;
            }
        }
    }

    public boolean isEven(int n){
        return (n & 1) == 0;
    }
}

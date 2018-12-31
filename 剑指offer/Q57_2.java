import java.util.ArrayList;

public class Q57_2 {
    public ArrayList<ArrayList<Integer>> FindContinuousSequence(int sum) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        int l=1, r=2;

        while (l<r && r<=sum/2+1){
            int t = (l+r)*(r-l+1)/2;
            if (t == sum){
                res.add(construct(l,r));
                r++;
                l++;
            }else if (t > sum){
                l++;
            }else{
                r++;
            }
        }
        return res;
    }

    public ArrayList<Integer> construct(int l, int r){
        ArrayList<Integer> res = new ArrayList<>();
        while (l<=r){
            res.add(l++);
        }
        return res;
    }
}

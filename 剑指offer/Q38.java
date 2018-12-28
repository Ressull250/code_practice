import java.util.*;

public class Q38 {
    public ArrayList<String> Permutation(String str) {
        ArrayList<String> res = new ArrayList<>();
        if (str == null || str.length() == 0) return res;
        char[] strs = str.toCharArray();
        Arrays.sort(strs);

        Set<String> set = new TreeSet<>();
        helper(strs, 0, set);
        return new ArrayList<>(set);
    }

    public void helper(char[] strs, int offset, Set<String> res){
        if (offset == strs.length){
            res.add(new String(strs));
        }
        for (int i=offset; i<strs.length; i++){
            swap(strs, i, offset);
            helper(strs, offset+1, res);
            swap(strs, i, offset);
        }
    }

    public void swap(char[] chars, int i, int j){
        char t = chars[i];
        chars[i] = chars[j];
        chars[j] = t;
    }
}

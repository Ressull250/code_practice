public class Q33 {

    public boolean VerifySquenceOfBST(int [] sequence) {
        if (sequence == null || sequence.length == 0) return true;
        return helper(sequence, 0, sequence.length, Integer.MAX_VALUE, Integer.MIN_VALUE);
    }

    public boolean helper(int[] sequcence, int l, int r, int max, int min){
        if (r<=l) return true;
        int middle = sequcence[r-1];
        if (middle > max || middle < min) return false;

        int t = l;
        while (t<r-1 && sequcence[t]<middle){
            if (sequcence[t] > max || sequcence[t] < min) return false;
            t++;
        }
        int tmp = t;
        while (tmp<r-1){
            if (sequcence[tmp] > max || sequcence[tmp] < min) return false;
            tmp++;
        }

        return helper(sequcence, l, t, middle, min) && helper(sequcence, t, r-1, max, middle);
    }
}
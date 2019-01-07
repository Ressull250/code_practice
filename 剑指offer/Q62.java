public class Q62 {
    public int LastRemaining_Solution(int n, int k) {
        if (n<=0 || k<=0) return -1;
        int last = 0;
        for (int i=2; i<=n; i++){
            last = (last+k)%i;
        }
        return last;
    }
}

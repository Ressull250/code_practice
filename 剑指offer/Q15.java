public class Q15 {
    public int NumberOf1_0(int n) {

        int t=1, count=0;
        for (int i=0; i<32; i++){
            count += ((n&t) == 0 ? 0 : 1);
            t <<= 1;
        }
        return count;
    }

    public int NumberOf1(int n) {

        int count = 0;
        while (n!=0){
            count++;
            //将最右边的1变成0
            n = (n-1) & n;
        }
        return count;
    }
}

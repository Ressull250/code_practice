public class Q65 {
    public int Add(int num1,int num2) {
        int c = 0;
        int res = 0;
        for (int i=0; i<32; i++){
            int a = (num1&(1<<i)) == 0 ? 0 : 1;
            int b = (num2&(1<<i)) == 0 ? 0 : 1;

            res += (((a+b+c)%2) << i);
            c = (a+b+c)/2;
        }
        return res;
    }
}

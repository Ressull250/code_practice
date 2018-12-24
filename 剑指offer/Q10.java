public class Q10 {
    public int Fibonacci(int n) {
        int f1=1,f2=1,f3=0;
        if (n <= 0)
            return 0;
        if (n==1 || n==2){
            return 1;
        }

        for (int i=2; i<n; i++){
            f3 = f2 + f1;
            f2 = f3;
            f1 = f2;
        }
        return f3;
    }
}

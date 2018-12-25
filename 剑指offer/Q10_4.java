public class Q10_4 {
    public int JumpFloor(int target) {
        int f1=1,f2=2,f3=0;
        if (target == 2)
            return 2;
        if (target == 1)
            return 1;

        for (int i=2; i<target; i++){
            f3 = f2 + f1;
            f1 = f2;
            f2 = f3;
        }
        return f3;
    }
}

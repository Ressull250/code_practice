public class Q10_3 {
    //不要用小矩形增加形成大矩形，比较复杂
    //用小矩形去覆盖面积已确定的大矩形
    //f(n) = f(n-1) + f(n-2);
    public int RectCover(int target) {
        int f1=1,f2=2,f3=0;
        if (target == 1)
            return 1;
        if (target == 2)
            return 2;

        for (int i=2; i<target; i++){
            f3 = f2 + f1;
            f1 = f2;
            f2 = f3;
        }
        return f3;
    }
}

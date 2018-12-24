public class Q10_2 {

    //f(n) = f(n-1) + f(n-2) + ... + f(1) + 1
    //f(n) = 2f(n-2)
    //f(1) = 1, f(2) = 2
    //等比数列求和 f(n) = 2^(n-1)
    public int JumpFloorII(int target) {
        return 1 << (target-1);
    }
}

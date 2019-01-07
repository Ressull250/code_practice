import jdk.management.resource.internal.inst.FileOutputStreamRMHooks;
import sun.awt.geom.AreaOp;

public class Q66 {
    public int[] multiply(int[] A) {
        if (A == null || A.length == 0) return null;
        int res[] = new int[A.length];
        res[0] = 1;
        for (int i=1; i<A.length; i++){
            res[i] = res[i-1]*A[i-1];
        }

        int t=1;
        for (int i=A.length-1; i>=0; i--){
            if (i == A.length-1)
                continue;
            t *= A[i+1];
            res[i] *= t;
        }
        return res;
    }
}

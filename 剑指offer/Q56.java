public class Q56 {

    public void FindNumsAppearOnce(int [] array, int num1[], int num2[]) {

        if (array == null || array.length == 0) return;
        int t=diff(array);

        int i=0;
        for (; i<32; i++){
            if (check(t, i))
                break;
        }
        t=i;
        num1[0] = num2[0] = 0;
        for (i=0; i<array.length; i++){
            if (check(array[i], t))
                num1[0]^=array[i];
            else
                num2[0]^=array[i];
        }
        if (num2[0] < num1[0]){
            t=num1[0];
            num1[0]=num2[0];
            num2[0]=t;
        }
    }

    public int diff(int array[]){
        int t=0;
        for (int i=0; i<array.length; i++){
            t ^= array[i];
        }
        return t;
    }

    public boolean check(int num, int i){
        if ((num & (1<<i)) != 0)
            return true;
        return false;
    }
}
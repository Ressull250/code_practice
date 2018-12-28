public class Q39 {
    public int MoreThanHalfNum_Solution(int [] array) {
        if (array == null || array.length == 0) return 0;
        int times = 1;
        int num = array[0];
        for (int i=1; i<array.length; i++){
            if (times == 0){
                num = array[i];
                times = 1;
            }else if (num == array[i]){
                times ++;
            }else{
                times --;
            }
        }

        times = 0;
        for (int i=0; i<array.length; i++){
            if (num == array[i])
                times++;
        }

        return times > array.length/2 ? num : 0;
    }
}

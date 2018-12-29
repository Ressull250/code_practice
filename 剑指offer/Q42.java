public class Q42 {

    public int FindGreatestSumOfSubArray(int[] array) {

        int maxx = Integer.MIN_VALUE;
        int sofar = 0;
        for (int i=0; i<array.length; i++){
            sofar += array[i];
            maxx = Math.max(maxx, sofar);
            if (sofar < 0){
                sofar = 0;
            }
        }
        return maxx;
    }
}

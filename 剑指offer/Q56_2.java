public class Q56_2 {

    //数组一个数字出现1次，其余出现3次
    public int findSingleNumber(int[] array){
        int[] count = new int[32];
        for (int num : array){
            for (int j=0; j<32; j++){
                count[j] += (num & (1<<j)) == 0 ? 0 : 1;
            }
        }
        int res=0;
        for (int j=0; j<32; j++){
            if (count[j] % 3 != 0){
                res += (1<<j);
            }
        }
        return res;
    }
}

public class Q63 {
    public int maxProfit(int nums[]){
        if (nums == null || nums.length <= 1)
            return 0;

        int minbefore = nums[0];
        int maxval = 0;
        for (int i=1; i<nums.length; i++){
            maxval = Math.max(maxval, nums[i]-minbefore);
            minbefore = Math.min(minbefore, nums[i]);
        }
        return maxval;
    }
}

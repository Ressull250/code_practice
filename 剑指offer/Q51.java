public class Q51 {
    public int InversePairs(int [] array) {
        if (array == null || array.length <= 1) return 0;

        int[] helper = new int[array.length];
        for (int i=0; i<array.length; i++)
            helper[i] = array[i];
        int count = partition(array, helper, 0, array.length-1);
        return count;
    }

    public int partition(int[] array, int[] helper, int l, int r){
        if (r <= l) return 0;
        int mid = (r-l)/2 + l;
        int left = partition(helper, array, l, mid) % 1000000007;
        int right = partition(helper, array, mid+1, r) % 1000000007;
        int count = 0;

        int oldmid = mid;
        int i=r;
        while (mid >= l && r > oldmid){
            if (array[mid] > array[r]){
                count += (r-oldmid);
                count %= 1000000007;
                helper[i] = array[mid];
                mid--;
            }else{
                helper[i] = array[r];
                r--;
            }
            i--;
        }

        for (;mid >= l; i--, mid--){
            helper[i] = array[mid];
        }
        for (;r > oldmid; i--, r--){
            helper[i] = array[r];
        }

        return (count+left+right)%1000000007;
    }
}


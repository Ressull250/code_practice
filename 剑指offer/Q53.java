public class Q53 {
    public int GetNumberOfK(int [] array , int k) {
        if (array == null || array.length == 0) return 0;
        int l=0, r=array.length-1, mid=0;
        while (l<=r){
            mid = (r-l)/2 + l;
            if (array[mid] == k)
                break;
            else if (array[mid] > k)
                r = mid-1;
            else
                l = mid+1;
        }
        if (array[mid] == k){
            int count=0;
            int t = mid-1;
            while (t >= 0 && array[t] == k){
                t--;
                count++;
            }
            t = mid+1;
            while (t < array.length && array[t] == k){
                t++;
                count++;
            }
            return count+1;
        }
        return 0;
    }
}

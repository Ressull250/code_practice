public class Q11 {

    public int minNumberInRotateArray(int [] array) {

        if (array == null) return 0;
        int l=0, r=array.length-1;

        while (l <= r){
            if (r-l<=1){
                return array[l]<array[r]?array[l]:array[r];
            }
            int mid = (r-l)/2 + l;
            if (array[l] < array[r])
                r = mid - 1;
            else{
                if (array[mid] >= array[l])
                    l = mid;
                else
                    r = mid;
            }
        }

        return array[l];
    }
}

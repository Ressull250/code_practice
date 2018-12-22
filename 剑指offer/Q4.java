public class Q4 {

    public boolean Find(int target, int [][] array) {
        if (array == null || array.length == 0)
            return false;

        int m = array.length;
        int n = array[0].length;
        int i = 0, j = n-1;

        while (true){
            if (i >= m || j < 0)
                return false;
            if (target == array[i][j]){
                return true;
            }
            if (target > array[i][j]){
                i++;
            }else{
                j--;
            }
        }
    }
}

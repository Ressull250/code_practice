public class Q3 {

    //可以修改原数组的O(n)
    public boolean duplicate(int numbers[],int length,int [] duplication) {
        if(numbers == null || length <=0){
            return false;
        }

        for (int i=0; i<length; i++){
            int num = numbers[i];
            if (num == i || num >= length)
                continue;
            else{
                //find duplication
                while (num != i)
                    if (numbers[num] == num){
                        duplication[0] = num;
                        return true;
                    }else{
                        swap(numbers, i, num);
                        num = numbers[i];
                    }
            }
        }

        return false;
    }

    public static void swap(int numbers[], int i, int j){
        int t = numbers[i];
        numbers[i] = numbers[j];
        numbers[j] = t;
    }

    //不可以修改原数组
    //如果从1开始可以利用快慢指针探测环的思想,因为不存在为0的index,一定会有2个index指向同一值，故有一个环
    //参考leetcode287
    //从0开始可以2分，O(nlogn)
}

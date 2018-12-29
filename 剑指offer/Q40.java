import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;

public class Q40 {
    public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
        ArrayList<Integer> res = new ArrayList<>();
        if (input == null || input.length < k || input.length <= 0 || k<=0) return res;
        Queue<Integer> q = new PriorityQueue<>((a,b) -> a>b ? -1 : 1);

        for (int i=0; i<input.length; i++){
            int num = input[i];
            if (q.size() < k)
                q.add(num);
            else if (q.peek() > num){
                q.poll();
                q.add(num);
            }
        }

        while (!q.isEmpty()){
            res.add(q.poll());
        }
        Collections.reverse(res);
        return res;
    }
}

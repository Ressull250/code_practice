import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;

public class Q59 {
    //deque存下标
    public ArrayList<Integer> maxInWindows(int [] num, int size) {
        ArrayList<Integer> res = new ArrayList<>();
        if (num == null || size <= 0 || num.length < size) return res;

        Deque<Integer> deque = new ArrayDeque<>();
        for (int i=0; i<num.length; i++){

            while (!deque.isEmpty() && num[deque.peekLast()] <= num[i])
                deque.removeLast();
            deque.addLast(i);
            if (i-deque.peekFirst() >= size)
                deque.removeFirst();

            if (i>=size-1)
                res.add(num[deque.peekFirst()]);
        }

        return res;
    }

    //deque存数字
    public ArrayList<Integer> maxInWindows0(int [] num, int size) {
        ArrayList<Integer> res = new ArrayList<>();
        if (num == null || size <= 0 || num.length < size) return res;

        Deque<Integer> deque = new ArrayDeque<>();
        int maxNow = Integer.MIN_VALUE;
        for (int i=0; i<num.length; i++){
            int val = num[i];

            if (val >= maxNow){
                maxNow = val;
                while (!deque.isEmpty()){
                    deque.removeFirst();
                }
                deque.addLast(val);
            }else{
                deque.addLast(val);
                if (deque.size() > size){
                    //max被移出，找到新的max
                    if (deque.removeFirst() == maxNow){
                        maxNow = Integer.MIN_VALUE;
                        for (Integer t : deque)
                            maxNow = Math.max(t, maxNow);
                        while (!deque.isEmpty() && deque.peekFirst() != maxNow){
                            deque.removeFirst();
                        }
                    }
                }
            }

            if (i>=size-1)
                res.add(maxNow);
        }

        return res;
    }
}

import java.util.PriorityQueue;

public class Q41 {

    PriorityQueue<Integer> big = new PriorityQueue<>((a,b) -> a>b ? -1 : 1);
    PriorityQueue<Integer> small = new PriorityQueue<>();

    public void Insert(Integer num) {
        if (big.isEmpty()){
            big.add(num);
            return;
        }
        if (big.size() == small.size()){
            if (num > small.peek()){
                big.add(small.poll());
                small.add(num);
            }
            else{
                big.add(num);
            }
        }
        else{
            if (num >= big.peek()){
                small.add(num);
            }
            else{
                small.add(big.poll());
                big.add(num);
            }
        }
    }

    public Double GetMedian() {
        if (big.size() == 0)
            return 0.0;
        if (big.size() == small.size())
            return (double) (big.peek()+small.peek())/2;
        else
            return (double) big.peek();
    }

}
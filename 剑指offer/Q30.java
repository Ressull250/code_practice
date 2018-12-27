import java.util.Stack;

public class Q30 {

    //负数会有溢出，不过测例好像没有负数
    Stack<Integer> s = new Stack<>();
    int min = Integer.MAX_VALUE;

    public void push(int node) {
        s.push(node - min);
        min = Math.min(node, min);
    }

    public void pop() {
        if (s.peek() <= 0){
            min -= s.peek();
        }
        s.pop();
    }

    public int top() {
        return s.peek() < 0 ? min : min+s.peek();
    }

    public int min() {
        return min;
    }
}

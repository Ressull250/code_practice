import java.util.Stack;

public class Q31 {
    public boolean IsPopOrder(int [] pushA,int [] popA) {
        if (pushA == null || popA == null) return false;
        if (pushA.length != popA.length) return false;

        Stack<Integer> stack = new Stack<>();
        int j=0;
        for (int i=0; i<popA.length; i++){
            //与栈顶元素相等
            if (!stack.empty() && stack.peek() == popA[i]){
                stack.pop();
                continue;
            }
            //继续压栈
            while (j<popA.length && popA[i] != pushA[j]){
                stack.push(pushA[j]);
                j++;
            }
            //没有找到相同元素，返回false
            if (j>=popA.length || popA[i] != pushA[j]){
                return false;
            }else{
                j++;
            }
        }
        return true;
    }
}
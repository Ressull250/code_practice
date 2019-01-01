import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;

public class Q100 {
    //从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
    ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        if (pRoot == null) return res;

        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(pRoot);
        while (!queue.isEmpty()){
            ArrayList<Integer> t = new ArrayList<>();
            for (int i=0,j=queue.size(); i<j; i++){
                TreeNode node = queue.poll();
                t.add(node.val);
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            res.add(t);
        }
        return res;
    }
}

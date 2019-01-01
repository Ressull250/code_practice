import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Queue;

public class Q101 {
    //请实现一个函数按照之字形打印二叉树，
    //即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，
    //其他行以此类推。
    public ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        if (pRoot == null) return res;

        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.add(pRoot);
        int level=0;
        while (!queue.isEmpty()){
            ArrayList<Integer> t = new ArrayList<>();
            for (int i=0,j=queue.size(); i<j; i++){
                TreeNode node = queue.poll();
                t.add(node.val);
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            if (level%2!=0)
                Collections.reverse(t);
            res.add(t);
            level++;
        }
        return res;
    }
}

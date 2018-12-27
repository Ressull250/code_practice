import java.util.*;

public class Q32 {
    public ArrayList<Integer> PrintFromTopToBottom(TreeNode root) {
        if (root == null) return new ArrayList<>();

        ArrayList<Integer> res = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()){
            TreeNode t = queue.poll();
            res.add(t.val);
            if (t.left != null) queue.add(t.left);
            if (t.right != null) queue.add(t.right);
        }

        return res;
    }
}
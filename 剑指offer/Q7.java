import java.util.Arrays;

public class Q7 {

    public TreeNode reConstructBinaryTree(int [] pre, int [] in) {
        return constructTree(pre, in);
    }

    public TreeNode constructTree(int[] pre, int[] in){
        if (pre.length == 0) return null;
        TreeNode head = new TreeNode(pre[0]);

        int i = 0;
        while (in[i] != pre[0] && i<in.length)
            i++;

        head.left = constructTree(Arrays.copyOfRange(pre, 1, i+1), Arrays.copyOfRange(in, 0, i));
        head.right = constructTree(Arrays.copyOfRange(pre, i+1, pre.length), Arrays.copyOfRange(in, i+1, in.length));
        return head;
    }

    class TreeNode{
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val){
            this.val = val;
        }
    }

}


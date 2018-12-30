public class Q55_2 {
    public boolean IsBalanced_Solution(TreeNode root) {
        return mydepth(root) != -1;
    }

    public int mydepth(TreeNode node){
        if (node == null) return 0;
        int left = mydepth(node.left);
        int right = mydepth(node.right);
        if (left == -1 || right == -1 || Math.abs(left-right) > 1)
            return -1;
        return left > right ? left+1 : right+1;
    }
}
public class Q27 {
    public void Mirror(TreeNode root) {
        if (root == null) return;
        TreeNode t = root.right;
        root.right = root.left;
        root.left = t;
        Mirror(root.left);
        Mirror(root.right);
    }
}

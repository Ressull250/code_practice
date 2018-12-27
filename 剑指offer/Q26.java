public class Q26 {
    public boolean HasSubtree(TreeNode root1,TreeNode root2) {
        if (root1 == null || root2 == null)
            return false;
        return helper(root1, root2);
    }

    public boolean helper(TreeNode t1, TreeNode t2){
        return isSame(t1, t2)
                || (t1.left != null && helper(t1.left, t2))
                || (t1.right != null && helper(t1.right, t2));
    }

    public boolean isSame(TreeNode t1, TreeNode t2){
        if (t1 == null && t2 == null) return true;
        if (t1 != null && t2 == null) return true;
        if (t1 == null && t2 != null) return false;
        return t1.val == t2.val && isSame(t1.left, t2.left) && isSame(t1.right, t2.right);
    }
}

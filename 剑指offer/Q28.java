public class Q28 {
    boolean isSymmetrical(TreeNode pRoot) {
        if (pRoot == null) return false;
        return helper(pRoot.left, pRoot.right);
    }

    boolean helper(TreeNode l, TreeNode r){
        if (l == null && r ==null) return true;
        if (l == null || r ==null) return false;
        return l.val == r.val && helper(l.right, r.left) && helper(l.left, r.right);
    }
}

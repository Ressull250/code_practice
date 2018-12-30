public class Q54 {

    TreeNode KthNode(TreeNode pRoot, int k) {
        int[] t = {k};
        return helper(pRoot, t);
    }

    TreeNode helper(TreeNode pRoot, int[] k){
        if (pRoot == null) return null;
        TreeNode left = helper(pRoot.left, k);
        if (left != null) return left;
        k[0]--;
        if (k[0]==0) return pRoot;
        TreeNode right = helper(pRoot.right, k);
        if (right != null) return right;
        return null;
    }
}

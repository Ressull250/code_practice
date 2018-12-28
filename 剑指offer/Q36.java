public class Q36 {

    public TreeNode Convert(TreeNode pRootOfTree) {
        return construct(pRootOfTree, false);
    }

    public TreeNode construct(TreeNode node, boolean isLeftTree){
        if (node == null) return null;
        if (node.left == null && node.right == null) return node;

        TreeNode left = construct(node.left, true);
        TreeNode right = construct(node.right, false);

        if (left == null){
            node.left = null;
        }else {
            node.left = left;
            left.right = node;
        }

        if (right == null){
            node.right = null;
        }else {
            node.right = right;
            right.left = node;
        }

        if (isLeftTree){
            while (node.right != null)
                node = node.right;
        }
        else {
            while (node.left != null)
                node = node.left;
        }

        return node;
    }
}

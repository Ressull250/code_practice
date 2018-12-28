public class Q37 {
    int offset = 0;

    String Serialize(TreeNode root) {
        return serializeHelper(root);
    }

    TreeNode Deserialize(String str) {
        offset = 0;
        String[] strs = str.split(",");
        return deserializeHelper(strs);
    }

    public String serializeHelper(TreeNode root){
        if (root == null) return "#,";
        String s = "";
        s += root.val + ",";
        s += serializeHelper(root.left);
        s += serializeHelper(root.right);
        return s;
    }

    public TreeNode deserializeHelper(String[] str) {
        if (str[offset].equals("#")){
            offset++;
            return null;
        }
        TreeNode node = new TreeNode(Integer.parseInt(str[offset]));
        offset++;
        node.left = deserializeHelper(str);
        node.right = deserializeHelper(str);
        return node;
    }
}

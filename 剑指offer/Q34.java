import java.util.ArrayList;

public class Q34 {
    public ArrayList<ArrayList<Integer>> FindPath(TreeNode root, int target) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        find(root, target, res, new ArrayList<>());
        return res;
    }

    public void find(TreeNode node, int target, ArrayList<ArrayList<Integer>> res, ArrayList<Integer> path){
        if (node == null) return;
        target -= node.val;
        ArrayList<Integer> newpath = copyAndAdd(path, node.val);
        if (node.left == null && node.right == null && target == 0){
           res.add(newpath);
           return;
        }

        find(node.left, target, res, newpath);
        find(node.right, target, res, newpath);
    }

    public ArrayList<Integer> copyAndAdd(ArrayList<Integer> list, int adder){
        ArrayList<Integer> res = new ArrayList<>(list);
        res.add(adder);
        return res;
    }
}

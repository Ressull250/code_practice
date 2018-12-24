


public class Q8 {
    public TreeLinkNode GetNext(TreeLinkNode p) {

        if (p == null) return null;
        //右子树为空，找爹
        if (p.right == null){
            if (p.next == null) return null;
            //爹的左儿
            if (p == p.next.left){
                return p.next;
            }
            //爹的右儿
            else{
                while (p == p.next.right){
                    p = p.next;
                    if (p.next == null) return null;
                }
                return p.next;
            }
        }
        //右子树不为空，前序
        else{
            return first(p.right);
        }
    }

    public TreeLinkNode first(TreeLinkNode p){
        while (p.left != null){
            p = p.left;
        }
        return p;
    }
}

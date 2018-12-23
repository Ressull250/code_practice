import java.util.ArrayList;

public class Q6 {

    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {

        ListNode dummy = new ListNode();
        ListNode nextNode;
        dummy.next = listNode;

        while (listNode != null && listNode.next != null){
            nextNode = listNode.next;
            ListNode t = nextNode.next;
            nextNode.next = dummy.next;
            dummy.next = nextNode;
            listNode.next = t;
        }

        ArrayList<Integer> res = new ArrayList<>();
        while (dummy.next != null){
            res.add(dummy.next.val);
            dummy = dummy.next;
        }
        return res;
    }

    class ListNode {
        int val;
        ListNode next = null;
    }
}
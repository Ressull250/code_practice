public class Q22 {

    public ListNode FindKthToTail(ListNode head, int k) {
        ListNode slow=head, fast=head;
        if (k<0 || fast == null) return null;
        for (int i=0; i<k-1; i++){
            if (fast.next == null)
                return null;
            fast = fast.next;
        }

        while (fast.next != null){
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}

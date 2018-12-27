public class Q23 {

    public ListNode EntryNodeOfLoop(ListNode pHead) {
        if (pHead == null || pHead.next == null) return null;
        ListNode slow=pHead.next;
        ListNode fast=pHead.next.next;

        while (slow != fast && fast!=null && fast.next!=null){
            slow = pHead.next;
            fast = fast.next.next;
        }
        //无环
        if (slow != fast) return null;

        while (pHead != fast){
            pHead = pHead.next;
            fast = fast.next;
        }

        return fast;
    }
}

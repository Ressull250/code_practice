public class Q24 {

    //这是比较常见的写法
    public ListNode ReverseList(ListNode head) {
        ListNode prev = null;

        while (head != null){
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }

        return prev;
    }

    //我一直以来的写法
    public ListNode ReverseList_1(ListNode head) {
        if (head == null) return null;
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        while (head.next != null){
            ListNode next = head.next;
            head.next = next.next;
            next.next = dummy.next;
            dummy.next = next;
        }

        return dummy.next;
    }
}

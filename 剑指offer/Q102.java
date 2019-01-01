public class Q102 {

    //在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
    //例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
    public ListNode deleteDuplication(ListNode pHead) {
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        dummy.next = pHead;
        ListNode last = dummy;
        while (pHead != null){
            ListNode t = pHead;
            while (pHead.next != null && pHead.val == pHead.next.val){
                pHead = pHead.next;
            }
            if (t == pHead){
                last = t;
            }
            else{
                last.next = pHead.next;
            }

            pHead = pHead.next;
        }
        return dummy.next;
    }
}

import java.util.List;

public class Q25 {
    public ListNode Merge(ListNode list1,ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode pre = dummy;
        while (list1 != null && list2 != null){
            if (list1.val < list2.val){
                pre.next = list1;
                list1 = list1.next;
            }else {
                pre.next = list2;
                list2 = list2.next;
            }
            pre = pre.next;
        }

        pre.next = null;
        if (list1 != null){
            pre.next = list1;
        }
        if (list2 != null){
            pre.next = list2;
        }

        return dummy.next;
    }
}

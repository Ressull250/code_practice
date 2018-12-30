public class Q52 {
    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if (pHead1 == null || pHead2 == null) return null;
        int len1=0, len2=0;
        ListNode t = pHead1;
        while (t!=null){
            len1++;
            t = t.next;
        }
        t = pHead2;
        while (t!=null){
            len2++;
            t = t.next;
        }

        if (len1 > len2){
            for (int i=0; i<len1-len2; i++)
                pHead1 = pHead1.next;
        }else if (len2 > len1){
            for (int i=0; i<len2-len1; i++)
                pHead2 = pHead2.next;
        }
        while (pHead1 != pHead2){
            pHead1 = pHead1.next;
            pHead2 = pHead2.next;
        }

        return pHead1;
    }

}

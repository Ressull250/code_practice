import java.util.HashMap;

public class Q35 {
    public RandomListNode Clone0(RandomListNode pHead) {
        RandomListNode dummy = new RandomListNode(-1);
        RandomListNode t = dummy;
        RandomListNode n = pHead;
        HashMap<RandomListNode, RandomListNode> map = new HashMap<>();

        while (n != null) {
            t.next = new RandomListNode(n.label);
            map.put(n, t.next);
            n = n.next;
            t = t.next;
        }

        t = dummy.next;
        while (pHead != null) {
            t.random = map.get(pHead.random);
            pHead = pHead.next;
            t = t.next;
        }

        return dummy.next;
    }

    public RandomListNode Clone(RandomListNode pHead) {
        if (pHead == null) return null;
        RandomListNode t = pHead;

        while (t!=null){
            RandomListNode next = t.next;
            t.next = new RandomListNode(t.label);
            t.next.next = next;
            t = next;
        }

        //t保存新的队列首
        t = pHead;
        while (t != null){
            t.next.random = t.random == null ? null : t.random.next;
            t = t.next.next;
        }

        t = pHead;
        RandomListNode node = pHead.next;
        while (true){
            RandomListNode next = t.next;
            t.next = next.next;
            if (next.next == null)
                break;
            next.next = t.next.next;
            t = t.next;
        }

        return node;
    }
}
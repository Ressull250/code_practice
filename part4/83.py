# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head;
        n = ListNode(0)
        n.next = head
        last = head.val;
        while head.next:
            if head.next.val == last:
                head.next = head.next.next;
            else:
                head = head.next;
                last = head.val
        return n.next;

head = ListNode(1)
# head.next = ListNode()
# head.next.next = ListNode(1)
new = Solution().deleteDuplicates(head)
new = 1




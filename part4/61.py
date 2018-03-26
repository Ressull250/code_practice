# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        if not head.next: return head

        len = 1
        p = head
        newhead = head
        secHead = head

        while p.next:
            p = p.next
            len += 1

        if k%len == 0: return head
        for _ in range(k%len):
            newhead = newhead.next

        while newhead.next:
            newhead = newhead.next
            secHead = secHead.next

        tmp = secHead.next
        secHead.next = None
        newhead.next = head

        return tmp

print Solution().rotateRight(ListNode(1),9)


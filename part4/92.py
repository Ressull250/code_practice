# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head: return head
        if not head.next: return head
        newhead = ListNode(0)
        newhead.next = head
        pre = newhead

        for i in range(m-1):
            pre = pre.next

        start = pre
        p = bftail = pre.next
        tail = p.next

        for i in range(n-m):

            start.next = tail
            bftail.next = tail.next
            tail.next = p

            tail = bftail.next
            p = start.next

        return newhead.next

a = ListNode(3)
a.next = ListNode(5)
# a.next.next = ListNode(3)
# a.next.next.next = ListNode(4)
# a.next.next.next.next = ListNode(5)

Solution().reverseBetween(a, 1, 2)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        nNode = start = head
        for _ in range(n):
            start = start.next

        if start is None:
            return head.next
        while start.next is not None:
            start = start.next
            nNode = nNode.next

        nNode.next = nNode.next.next


        return head

a = ListNode(0)
a.next = ListNode(1)
a.next.next = ListNode(2)
a.next.next.next = ListNode(3)

a = Solution().removeNthFromEnd(a,4)
a = None

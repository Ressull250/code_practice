class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head: return head
        first = f1 = ListNode(0)
        second = s2 = ListNode(0)

        while head:
            if head.val < x:
                f1.next = head
                f1 = f1.next
            else:
                s2.next = head
                s2 = s2.next
            head = head.next

        s2.next = None
        f1.next = second.next
        return first.next

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
new = Solution().partition(head,3)
new = 1
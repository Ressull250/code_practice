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
        n = ListNode(0)
        n.next = head
        last = n
        while head and head.next:
            if head.val == head.next.val:
                p = head.next
                while p.next and p.next.val == head.val:
                    p = p.next
                last.next = p.next
                head = p.next
            else:
                last = head
                head = head.next;

        return n.next;

head = ListNode(2)
head.next = ListNode(2)
head.next.next = ListNode(3)
new = Solution().deleteDuplicates(head)
new = 1
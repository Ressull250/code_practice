# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        while head and head.next:
            tmp = head.val
            head.val = head.next.val
            head.next.val = tmp
            head = head.next.next

        return start

a = ListNode(1)



Solution().swapPairs(None)
# # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # fan zhuan
        last = ListNode(0)
        last.next = slow.next
        cur = slow.next
        slow.next = None

        while cur and cur.next:
            next = cur.next
            cur.next = next.next
            t = last.next
            last.next = next
            next.next = t

        # cha ru
        begin = last.next
        h1 = head
        while begin:
            t = h1.next
            h1.next = begin
            t2 = begin.next
            begin.next = t
            begin = t2
            h1 = t




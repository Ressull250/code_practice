# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import sys
class Solution(object):
    def insertionSortList(self, head):
        cur = dummy = ListNode(0)
        while head:
            if cur and cur.val > head.val:  # reset pointer only when new number is smaller than pointer value
                cur = dummy
            while cur.next and cur.next.val < head.val:  # classic insertion sort to find position
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next  # insert
        return dummy.next



a = ListNode(2)
a.next = ListNode(3)
a.next.next = ListNode(1)
Solution().insertionSortList(a)


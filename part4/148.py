# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, x):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sort(head):
            if not head or not head.next: return head
            prev = None
            slow = fast = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev: prev.next = None
            p1 = sort(head)
            p2 = sort(slow)
            return merge(p1, p2)

        def merge(left, right):
            dummy = p = ListNode(0)
            while left or right:
                if left and right:
                    if left.val < right.val:
                        p.next = left
                        left = left.next
                    else:
                        p.next = right
                        right = right.next
                else:
                    if left:
                        p.next = left
                        left = left.next
                    else:
                        p.next = right
                        right = right.next
                p = p.next
            return dummy.next

        return sort(x)




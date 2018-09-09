# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        t1,t2 = headA,headB

        while t1 != t2:
            t1 = t1.next if t1 else headB
            t2 = t2.next if t2 else headA

        return t1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0;
        tmpnode = head = ListNode(0)
        while not (l1 is None and l2 is None):
            num1 = 0;
            num2 = 0;
            if l1 is not None:
                num1 = l1.val
                l1 = l1.next
            if l2 is not None:
                num2 = l2.val
                l2 = l2.next
            tmpnode.next = ListNode((num1+num2+c)%10)
            c = (num1+num2+c)//10
            tmpnode = tmpnode.next

        if c == 1:
            tmpnode.next = ListNode(1)

        return head.next

l1 = ListNode(3)
l2 = ListNode(8)
l3 = Solution().addTwoNumbers(l1,l2)
l4 = None
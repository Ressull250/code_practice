class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        slow = self.reverseList0(slow)

        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        else:
            return True

    def reverseList0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        last = None

        while head:
            next = head.next
            head.next = last
            last = head
            head = next

        return last


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow and slow == fast:
                return True
        return False
class Solution:
    # iterative
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

    # recursive
    def reverseList(self, head):
        def reverse(head, newhead):
            if not head:
                return newhead
            t = head.next
            head.next = newhead
            return reverse(t, head)

        newhead = None
        return reverse(head, newhead)




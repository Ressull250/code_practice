#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0 :
            return []
        elif len(lists) == 1:
            return lists[0]

        tlists = list()
        while len(lists) != 1:
            tlists = list(); i = 0
            while i < len(lists):
                if i+1 < len(lists):
                    tlists.append(self.mergeTwoLists(lists[i],lists[i+1]))
                    i += 2
                else:
                    tlists.append(lists[i])
                    break

            lists = tlists

        return tlists[0]

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1:
            node.next = l1

        if l2:
            node.next = l2

        return head.next

a=ListNode(0)
a.next = ListNode(2)
a.next.next = ListNode(4)

b = ListNode(-1)

c=ListNode(3)
c.next = ListNode(6)

lists = [a,b,c]
print(Solution().mergeKLists(lists))
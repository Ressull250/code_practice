# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        map = {}
        t = head
        while t:
            map[t] = RandomListNode(t.label)
            t = t.next

        t = head
        while t:
            map[t].next = map.get(t.next)
            map[t].random = map.get(t.random)
            t = t.next

        return map[head]
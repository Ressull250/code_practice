# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def build(nums):
            if not nums: return None
            n = len(nums)/2
            root = TreeNode(nums[n])
            l = build(nums[0:n])
            r = build(nums[n+1:])
            root.left = l
            root.right = r
            return root
        list = []
        while head:
            list.append(head.val)
            head = head.next
        return build(list)


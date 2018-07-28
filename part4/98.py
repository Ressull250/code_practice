# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def judge(root, l, r):
            if not root: return True
            if not (l<root.val<r): return False
            return judge(root.left, l, root.val) and judge(root.right, root.val, r)

        return judge(root, -sys.maxint, sys.maxint)

a = TreeNode(2)
a.left = TreeNode(1)
a.right = TreeNode(3)

Solution().isValidBST(a)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
class Solution(object):
    maxval = -sys.maxsize
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node: return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.maxval = max(self.maxval, node.val + left + right)
            return node.val + max(left,right)

        dfs(root)
        return self.maxval
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(root, path):
            if not root: return path
            return max(find(root.left, path+1), find(root.right, path+1))

        return find(root, 0)

a = TreeNode(1)
# a.left = TreeNode(2)
# a.right = TreeNode(3)
# a.right.right = TreeNode(4)
print(Solution().maxDepth(a))
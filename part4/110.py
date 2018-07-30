class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(root, path):
            if not root: return path
            return max(find(root.left, path+1), find(root.right, path+1))

        return find(root, 0)
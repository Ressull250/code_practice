class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find(root, path):
            if not root: return path
            if root.left and root.right: return min(find(root.left, path+1), find(root.right, path+1))
            if root.left or root.right: return find(root.left, path+1) if root.left else find(root.right, path+1)
            return path+1

        return find(root, 0)

a = TreeNode(1)
a.left = TreeNode(2)
print Solution().minDepth(a)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def find(root, path):
            if root:
                path.append(root.val)
                find(root.left, path)
                find(root.right, path)

        res = []
        find(root, res)
        return res


class Solution(object):
    def preorderTraversal(self, root):
        res,stack = [],[]

        while root or stack:
            if not root: root = stack.pop(-1)
            res.append(root.val)
            if root.right: stack.append(root.right)
            root = root.left

        return res
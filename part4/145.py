# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        stack,res = [],[]

        while root or stack:
            if root:
                stack.append(root.left)
                res.append(root.val)
                root = root.right
            else:
                root = stack.pop(-1)

        res.reverse()
        return res

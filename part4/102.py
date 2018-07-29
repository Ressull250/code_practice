# coding=utf8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res,t = [],[]
        stack = [None]
        while root or stack:
            # root为空，栈不空
            if root == 'end':
                break
            if not root:
                stack.append(None)
                res.append(t)
                t=[]
                root = stack.pop(0)
            # root非空
            else:
                t.append(root.val)
                if root.left: stack.append(root.left)
                if root.right: stack.append(root.right)
                if stack:
                    root = stack.pop(0)
                else:
                    root = 'end'
        if t: res.append(t)
        return res

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.right.right = TreeNode(4)
print(Solution().levelOrder(None))
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stk,levels,res = [root],[],[]
        while stk:
            t = []
            for i in range(len(stk)):
                node = stk.pop(0)
                t.append(node.val)
                if node.left: stk.append(node.left)
                if node.right: stk.append(node.right)
                levels.append(t)
        for level in levels:
            res.append(level[-1])
        return res
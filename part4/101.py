# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import copy
class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def switch(root):
            if root:
                root.left,root.right = root.right,root.left
                switch(root.left)
                switch(root.right)

        t = copy.deepcopy(root)
        switch(t)
        return self.isSameTree(t,root)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def judge(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val == r.val:
                return judge(l.left, r.right) and judge(l.right, r.left)
            else:
                return False

        if not root: return True
        return judge(root.left, root.right)
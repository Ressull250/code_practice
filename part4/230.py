# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        def dfs(node):
            if not node: return
            dfs(node.left)
            l.append(node.val)
            if len(l) >= k:
                return
            dfs(node.right)

        l = []
        dfs(root)
        return l[k-1]
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution0(object):
    def countNodes(self, root):
        if not root: return 0
        def leftDepth(node):
            if not node: return 0
            return leftDepth(node.left) + 1
        depth = leftDepth(root)
        lastlevelnodes = pow(2, depth-1)
        for i in reversed(range(1,depth)):
            # left subtree full
            if leftDepth(root.right) == i:
                root = root.right
            # left subtree notfull
            else:
                lastlevelnodes -= pow(2, i-1)
                root = root.left
        nodes = pow(2,depth-1) - 1 + lastlevelnodes
        return nodes

class Solution(object):
    def countNodes(self, root):
        if not root: return 0
        def leftDepth(node):
            if not node: return -1
            return leftDepth(node.left) + 1
        depth = leftDepth(root)
        if leftDepth(root.right) == depth - 1:
            return (1 << depth) + self.countNodes(root.right)
        else:
            return (1 << (depth-1)) + self.countNodes(root.left)
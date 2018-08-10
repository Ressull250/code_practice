class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bfs(node, sum, total):
            if not node: return
            sum = sum * 10 + node.val
            if node.right or node.left:
                bfs(node.left, sum, total)
                bfs(node.right, sum, total)
            if not node.left and not node.right:
                total[0] += sum

        t = [0]
        bfs(root, 0, t)
        return t[0]


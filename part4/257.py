# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def bfs(node, path):
            if not node.left and not node.right:
                res.append("->".join(path + [str(node.val)]))
            else:
                if node.left:
                    bfs(node.left, path + [str(node.val)])
                if node.right:
                    bfs(node.right, path + [str(node.val)])

        if not root: return []

        res = []
        bfs(root, [])
        return res

a =TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)

print Solution().binaryTreePaths(a)
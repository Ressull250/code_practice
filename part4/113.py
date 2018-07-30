class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def find(root, sum, path, res):
            if not root: return
            sum -= root.val
            if sum == 0 and not root.left and not root.right: res.append(path+[root.val])
            find(root.left, sum, path+[root.val], res)
            find(root.right, sum, path+[root.val], res)

        path, res = [],[]
        find(root, sum, path, res)
        return res
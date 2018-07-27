class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def expan(left, right):
            res = []
            if left > right: return [None]
            if left == right: return [TreeNode(left)]
            for i in range(left, right+1):
                llist = expan(left, i-1)
                rlist = expan(i+1, right)
                for l in llist:
                    for r in rlist:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return expan(1,n) if n!=0 else []

a = Solution().generateTrees(0)
a = 3

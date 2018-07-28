# coding:utf-8
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0: return 0
        g = [0 for _ in range(n+1)]
        g[0] = g[1] = 1

        for x in range(2,n+1):
            for i in range(1,x+1):
                g[x] += g[i-1]*g[x-i]

        return g[n]

print(Solution().numTrees(4))

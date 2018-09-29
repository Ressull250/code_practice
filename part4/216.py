class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def sumk(t, l, path):
            if t == 0 and sum(path) == n: res.append(path)
            for i in range(l,10):
                if i not in path and sum(path) + i <= n:
                    sumk(t-1, i+1, path+[i])
            pass
        res = []
        sumk(k, 1, [])
        return res

print Solution().combinationSum3(3,9)


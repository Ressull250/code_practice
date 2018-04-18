# -*- coding:utf-8 -*-
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.tb(1,n+1,k,[],res)
        return res

    def tb(self, c, n, k, tlist, res):
        if k==0:
            res.append(tlist)
            return
        for i in range(c,n):
            # 加了这行判断就好了
            if n-i-1<k-1: break
            self.tb(i+1, n, k-1, tlist+[i], res)

print(Solution().combine(20,16))
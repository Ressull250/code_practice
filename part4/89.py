# -*- coding:utf-8 -*-
class Solution:
    def grayCode(self, n):
        # 找规律
        # i = 1   0 1
        # i = 2   00 01 11 10
        # i = 3   000 001 011 010 110 111 101 100
        res = [0]
        for i in range(n):
            res += [x + pow(2,i) for x in reversed(res)]
        return res
print(Solution().grayCode(5))
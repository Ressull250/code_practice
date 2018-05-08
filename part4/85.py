# -*- coding:utf-8 -*-
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        maxsize = 0
        row = [0 for _ in range(len(matrix[0]))]
        for i in matrix:
            for j,val in enumerate(i):
                if val == '1':
                    row[j]+=1
                else:
                    row[j]=0
            maxsize = max(maxsize,self.largestRectangleArea(row))
        return maxsize


    # leetcode84题
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()
        heights.append(0)
        maxsize = 0
        for i,h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                high = heights[stack.pop()]

                cpos = stack[-1] if stack else -1
                width = i - cpos - 1
                maxsize = max(maxsize,high*width)
            stack.append(i)
        return maxsize

print Solution().maximalRectangle([[],[]])
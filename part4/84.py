class Solution(object):
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

print(Solution().largestRectangleArea([]))

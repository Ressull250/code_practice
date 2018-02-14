class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0; r = len(height)-1
        maxArea = 0;
        while l<r :
            maxArea = max((r-l) * min(height[l],height[r]), maxArea)
            if height[l]>height[r]:
                r -= 1
            else:
                l += 1

        return maxArea

print(Solution().maxArea([1,1]))


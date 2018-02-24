class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        if len(height) == 0: return 0
        maxl,maxr = [n for n in range(len(height))],[n for n in range(len(height))]
        maxl[0],maxr[-1] = height[0],height[-1]
        for i in range(1,len(height)):
            maxl[i] = max(height[i],maxl[i-1])
        for i in reversed(range(0,len(height)-1)):
            maxr[i] = max(height[i],maxr[i+1])
        for i in range(len(height)):
            ret += min(maxl[i],maxr[i]) - height[i]

        return ret

print(Solution().trap([2,1,2]))
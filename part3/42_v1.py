#TLE
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(1,len(height)-1):
            maxleft, maxright = 0, 0
            for j in range(0,i+1):
                maxleft = max(maxleft, height[j])
            for j in range(i,len(height)):
                maxright = max(maxright, height[j])
            ret += min(maxright,maxleft) - height[i]

        return ret

print(Solution().trap([2,1,2]))

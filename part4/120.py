class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return 0
        n = len(triangle)
        for i in reversed(range(n)):
            for j in range(i):
                triangle[i-1][j] += min(triangle[i][j],triangle[i][j+1])

        return triangle[0][0]


print Solution().minimumTotal([
])

import sys
class Solution(object):
    dp = []
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(self.dp) < n+1:
            self.dp = [sys.maxsize for _ in range(n+1)]

        dp = self.dp
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        return dp[n]

print Solution().numSquares(12)
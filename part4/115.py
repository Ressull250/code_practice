class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n,m = len(t),len(s)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i==j==0: dp[0][0] = 1
                elif i==0: dp[i][j] = 1
                elif j==0: dp[i][j] = 0
                elif s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[n][m]

Solution().numDistinct("rabbbit","")
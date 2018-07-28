class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m,n = len(s1),len(s2)
        if m+n != len(s3): return False
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]

        dp[0][0] = True
        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j==0:
                    dp[0][0] = True
                elif i==0:
                    dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
                elif j==0:
                    dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[m][n]

print Solution().isInterleave("","","")
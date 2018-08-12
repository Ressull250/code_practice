class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [i-1 for i in range(n+1)]
        for i in range(n):
            j=0
            while i-j>=0 and j+i<n and s[i-j] == s[j+i]:
                dp[i+j+1] = min(dp[i+j+1], dp[i-j]+1)
                j+=1

            j=1
            while i-j+1>=0 and j+i<n and s[i-j+1] == s[j+i]:
                dp[i+j+1] = min(dp[i+j+1], dp[i-j+1]+1)
                j+=1
        return dp

print(Solution().minCut(""))

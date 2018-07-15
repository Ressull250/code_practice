class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = [0]
        dp = [0 for _ in range(len(s)+1)]
        for i in range(len(s)):
            if s[i] != '0':
                dp[i+1] = dp[i]+1
            if i-1>=0 and 10 <= int(s[i-1:i+1]) <= 26:
                print(int(s[i-1:i+1]))
                dp[i+1] = dp[i-1]+1

        print(dp[len(s)])
        return dp


print(Solution().numDecodings('2611'))
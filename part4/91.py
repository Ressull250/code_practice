# -*- coding:utf-8 -*-
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s)+1)]
        if s[0] == '0': return 0
        dp[0] = dp[1] = 1
        for i in range(1,len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            else:
                if 0<int(s[i-1:i+1])<=9:
                    dp[i+1] = dp[i-1]
                elif 10<=int(s[i-1:i+1])<=26:
                    dp[i+1] = dp[i] + dp[i-1]
                else:
                    dp[i+1] = dp[i]

        return dp[len(s)]



print(Solution().numDecodings('101'))
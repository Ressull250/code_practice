# -*- coding:utf-8 -*-
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        dp = [ [0 for _ in range(n+1)] for _ in range(m+1) ]

        for i in range(1,m+1): dp[i][0] = i
        for j in range(1,n+1): dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

        return dp[m][n]

print Solution().minDistance("sparta","part")

#
# 假设从 a b c d e -> f g h i
# 我们已知从 a b c d -> f g h
#
# replace:
#       将e替换成i,即是dp[i][j]=dp[i-1][j-1]+1
# delete:
#       将e删除，再将abcd转换到fghi的基础上删除e
#       即是dp[i][j]=dp[i-1][j]+1
# insert:
#       即知道abcde->fgh在abcde末尾插入i 使abcdei = fghi
#       即是dp[i][j]=dp[i][j-1]+1





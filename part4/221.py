class Solution(object):
    def maximalSquare0(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0

        m,n = len(matrix),len(matrix[0])
        maxsquare = 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0': continue
                dp[i+1][j+1] = min(dp[i][j],dp[i+1][j],dp[i][j+1])+1
                maxsquare = max(maxsquare, dp[i+1][j+1])
        return maxsquare*maxsquare

    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]: return 0

        m,n = len(matrix),len(matrix[0])
        maxsquare = 0
        dp = [0 for _ in range(n+1)]
        for i in range(m):
            prev = 0
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[j+1] = 0
                    continue
                tmp = dp[j+1]
                dp[j+1] = min(dp[j+1], prev, dp[j])+1
                maxsquare = max(maxsquare, dp[j+1])
                prev = tmp

        return maxsquare*maxsquare

print Solution().maximalSquare([['1','1'],['1','1']])
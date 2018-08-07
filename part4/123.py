class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        times = 2
        dp = [[0 for _ in range(len(prices))] for _ in range(times+1)]

        for i in range(1,times+1):
            tmp = dp[i-1][0] - prices[0]
            for j in range(1,len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j]+tmp)
                tmp = max(tmp, dp[i-1][j]-prices[j])

        return max(dp[times][len(prices)-1],0)

print Solution().maxProfit([])

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k==0: return 0
        if k>=len(prices)/2:
            res = 0
            for i in range(1,len(prices)):
                if prices[i] - prices[i-1] > 0:
                    res += prices[i] - prices[i-1]
            return res
        dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for i in range(1, k+1):
            tmp = dp[i-1][0] - prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j]+tmp)
                tmp = max(tmp, dp[i-1][j] - prices[j])

        return max(dp[k][len(prices)-1], 0)

print Solution().maxProfit(4, [1,2,3,4,5])
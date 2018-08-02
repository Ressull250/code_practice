class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxpro = maxnow = 0
        for i in range(1, len(prices)):
            maxnow = max(0, maxnow+prices[i]-prices[i-1])
            maxpro = max(maxnow, maxpro)
        return maxpro

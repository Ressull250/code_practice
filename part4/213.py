class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        def countMAX(begin, end):
            dp = [0 for _ in range(len(nums))]
            dp[begin] = nums[begin]
            for i in range(begin+1, end):
                if i == begin+1:
                    dp[begin+1] = max(nums[begin], nums[begin+1])
                else:
                    dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            return dp[end-1]

        return max(countMAX(0,len(nums)-1), countMAX(1, len(nums)))

print Solution().rob([1,2,3,1])
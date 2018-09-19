class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = total = 0
        n = len(nums)
        minlen = n + 1
        for i in range(n):
            total += nums[i]
            while total >= s:
                minlen = min(minlen, i - start + 1)
                total -= nums[start]
                start += 1
            pass
        return 0 if minlen == n + 1 else minlen




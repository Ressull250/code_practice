class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        summ = sum(nums)
        return n*(n+1)/2 - summ

print Solution().missingNumber([0,1,3])
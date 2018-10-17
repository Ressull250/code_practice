class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for _ in range(n)]
        for i in range(1,n):
            res[i] *= nums[i-1]*res[i-1]
        r = 1
        for i in reversed(range(0,n)):
            res[i] *= r
            r *= nums[i]
        return res

print Solution().productExceptSelf([1,2,3,4,5])

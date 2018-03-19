class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = [0 for _ in xrange(len(nums))];
        val = t[0] = nums[0]
        for i,num in enumerate(nums):
            if i > 0: t[i] = max(num, t[i-1]+num)
            if t[i] > val: val = t[i]

        return val

    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = t = nums[0]
        for i,num in enumerate(nums):
            if i > 0: t = max(num, t+num)
            if t > val: val = t

        return val


print Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4])
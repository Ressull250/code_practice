class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp

        for i in range(len(nums)):
            if nums[i]-1 != i:
                return i+1

        return len(nums)+1





print(Solution().firstMissingPositive([5]))

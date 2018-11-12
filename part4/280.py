class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i,num in enumerate(nums):
            if num == 0:
                count += 1
            else:
                nums[i-count], nums[i] = nums[i], nums[i-count]

Solution().moveZeroes([0,1,2,0,0,3,0])



class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        if len(nums) == 3: return max(nums[0]+nums[2], nums[1])

        nums[2] += nums[0]
        for i in range(3,len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        for i in range(1,len(nums)):
            if i == 1:
                nums[1] = max(nums[0], nums[1])
            else:
                nums[i] = max(nums[i-1], nums[i]+nums[i-2])
        return nums[-1]

print Solution().rob([100])
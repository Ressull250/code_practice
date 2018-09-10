class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 1:
            return 0
        nums.sort()
        maxx = -1
        for i,_ in enumerate(nums[1:]):
            maxx = max(abs(nums[i+1] - nums[i]), maxx)
        return maxx

print Solution().maximumGap([3,6,9,1])

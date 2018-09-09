class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        l,r = 0,len(nums)-1

        while l<r:
            mid = (l+r) / 2
            if nums[r] > nums[mid]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid+1
            else:
                r = r-1

        return nums[l]

print Solution().findMin([-1,-1,1])

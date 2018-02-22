import sys
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            num = nums[mid] if (target<nums[0]) == (nums[mid]<nums[0]) \
                    else (sys.maxsize if target>nums[0] else -sys.maxsize)

            if num < target:
                l = mid+1
            elif num > target:
                r = mid+1
            else:
                return mid

        return -1

print(Solution().search([3,1],2))

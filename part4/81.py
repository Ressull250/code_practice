# -*- coding:utf-8 -*-
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l + (r-l)/2
            if nums[mid] == target:
                return True

            #右半边order
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            #左半边order
            elif nums[mid] > nums[r]:
                if nums[mid] >= target > nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r-=1

        return False

print(Solution().search([3,5,1],3))
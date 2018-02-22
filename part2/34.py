class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0,len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid]<target:
                l = mid + 1
            elif nums[mid]>=target:
                r = mid - 1

        if nums == [] or l >= len(nums) or nums[l] != target:
            return [-1,-1]
        else:
            i = l
            while (i+1)<len(nums):
                if nums[i+1] != target:
                    break
                i+=1
            return [l,i]

print(Solution().searchRange([2,2],3))

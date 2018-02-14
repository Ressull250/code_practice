class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        res = list()
        for i in range(0,len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            left = i+1
            right = len(nums) - 1

            while left < right:
                current = nums[left] + nums[right]
                if target == current:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right:
                        if nums[left] == nums[left-1]:
                            left += 1
                        elif nums[right] == nums[right+1]:
                            right -= 1
                        else:
                            break
                elif target > current:
                    left += 1
                else:
                    right -= 1

        return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))
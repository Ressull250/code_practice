class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        dist = nums[0]+nums[1]+nums[2]-target
        for i in range(0,len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            targetN = target - nums[i]
            left = i+1
            right = len(nums) - 1

            while left < right:
                current = nums[left] + nums[right]
                if targetN == current:
                    return target
                elif abs(current - targetN) - abs(dist) < 0:
                    dist = current - targetN

                if current - targetN > 0:
                    right -= 1
                else:
                    left += 1

        return target+dist

print(Solution().threeSumClosest([-1,2,1,-4],1))

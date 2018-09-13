class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        k = k % len(nums)
        t1 = nums[0:len(nums) - k]
        t2 = nums[len(nums) - k:]
        for i in range(len(t2)):
            nums[i] = t2[i]
        for i in range(len(t1)):
            nums[i+len(t2)] = t1[i]
        print nums

Solution().rotate([1,2], 2)



class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.recurs(nums, res, [])
        return res


    def recurs(self, nums, lists, cnums):
        if len(nums) == 1:
            if cnums+nums not in lists:
                lists.append(cnums+nums)
        else:
            for i in range(len(nums)):
                t = nums.copy()
                t.remove(nums[i])
                self.recurs(t,lists,cnums+[nums[i]])
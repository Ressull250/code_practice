class Solution:
    def permute(self, nums):
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
                if i>=1 and nums[i-1] == nums[i]:

                t = nums.copy()
                t.remove(nums[i])
                self.recurs(t,lists,cnums+[nums[i]])

print(Solution().permute([1,1,2]))
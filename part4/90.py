class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        i = 0
        while i < len(nums):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                times,tmp = 1,[]
                while i+1 < len(nums) and nums[i] == nums[i+1]:
                    i += 1
                    times += 1
                for j in range(1,times+1):
                    tmp += ([ _ + [nums[i] for x in range(j)] for _ in res])
                res += tmp
            else:
                res += [j + [nums[i]] for j in res]

            i += 1
        return res

print Solution().subsetsWithDup([4,4,4,1,4])
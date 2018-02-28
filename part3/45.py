
class Solution:

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_maxpos,l_maxpos = 0,0
        level = 0
        for i in range(len(nums)-1):
            c_maxpos = max(c_maxpos, i+nums[i])
            if i == l_maxpos:
                level += 1
                l_maxpos = c_maxpos

        return level



print(Solution().jump([2,3,1,1,4]))


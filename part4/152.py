class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = maxx = minn = nums[0]
        for num in nums[1:]:
            if num < 0:
                maxx, minn = minn, maxx
            maxx = max(num, maxx*num)
            minn = min(num, minn*num)
            res = max(maxx, res)

        return res

print(Solution().maxProduct([2,-1,-3,6]))
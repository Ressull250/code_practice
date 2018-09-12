class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums: return '0'
        nums = sorted(map(str,nums), cmp=lambda a,b: 1 if a+b<b+a else -1)
        return ''.join(nums if nums[0] != '0' else ['0'])
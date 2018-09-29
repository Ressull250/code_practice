class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        last = 'X'
        for i in nums:
            if i == last:
                return True
            else:
                last = i
        return False

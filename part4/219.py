class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i,num in enumerate(nums):
            if num in dict and i - dict[num] <= k:
                return True
            dict[num] = i
        return False

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

print Solution().containsNearbyDuplicate([1,0,1,1], 1)

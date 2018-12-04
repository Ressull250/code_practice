class Solution(object):
    def findDuplicate0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)

    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return fast

print Solution().findDuplicate([3,1,3,4,2])
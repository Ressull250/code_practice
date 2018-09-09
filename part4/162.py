class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findpeak(list, l):
            if len(list) < 3: return -1
            mid = len(list) / 2
            if list[mid] > max(list[mid-1], list[mid+1]):
                return l + mid
            else:
                t1 = findpeak(list[0:mid+1], l)
                if t1 != -1:
                    return t1
                t2 = findpeak(list[mid:], l+mid)
                if t2 != -1:
                    return t2
                return -1
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        return findpeak(nums, 0)

print(Solution().findPeakElement([2,2,2,2,5,2]))




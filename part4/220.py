class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k<1 or t<0: return False
        dict = {}
        for i,num in enumerate(nums):
            bucket = num / (t+1)
            if bucket in dict or \
                    (bucket+1 in dict and dict[bucket+1] - num <= t) or \
                    (bucket-1 in dict and num - dict[bucket-1] <= t):
                return True
            if len(dict) >= k:
                dict.pop(nums[i-k]/(t+1))
            dict[bucket] = num
        return False

print Solution().containsNearbyAlmostDuplicate([1,2,3,1],
3,
0)






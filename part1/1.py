class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = dict()
        for i,num in enumerate(nums):
            key = target - num
            if num in map:
                return [map[num],i]
            else:
                map.update({key:i})


solu = Solution()
print(solu.twoSum([3,2,4],6))
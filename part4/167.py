class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        mset = {}
        for i in range(len(numbers)):
            if target-numbers[i] in mset:
                return [mset[target-numbers[i]]+1, i+1]
            else:
                mset[numbers[i]] = i


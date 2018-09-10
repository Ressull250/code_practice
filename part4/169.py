class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        maxx,index = 0,0
        for i in dic.keys():
            if dic[i] > maxx:
                maxx = dic[i]
                index = i

        return index
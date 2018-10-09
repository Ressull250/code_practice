class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        res = []
        start = last = 0
        for i,num in enumerate(nums):
            if i == 0:
                start = last = num
                continue
            if num == last+1:
                last += 1
            else:
                if last == start:
                    res.append(str(last))
                else:
                    res.append(str(start)+"->"+str(last))
                start = last = num
        if last == start:
            res.append(str(last))
        else:
            res.append(str(start) + "->" + str(last))
        return res



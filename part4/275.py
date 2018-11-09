class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i,num in enumerate(reversed(citations)):
            if num >= i+1:
                continue
            else:
                return i
        return len(citations)
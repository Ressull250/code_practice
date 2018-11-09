class Solution(object):
    def hIndex0(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        for i,num in enumerate(reversed(citations)):
            if num >= i+1:
                continue
            else:
                return i
        return len(citations)

    def hIndex(self, citations):
        n = len(citations)
        buk = [0 for _ in range(n+1)]
        for num in citations:
            if num > n:
                buk[n] += 1
            else:
                buk[num] += 1

        total = 0
        for i,num in enumerate(buk[::-1]):
            total += num
            if total >= n-i:
                return n-i

print Solution().hIndex([0])
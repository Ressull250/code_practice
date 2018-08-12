class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings: return 0
        n = len(ratings)
        c = [1 for _ in range(n)]
        sum = 0
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                c[i] = c[i-1]+1
        for i in reversed(range(n-1)):
            if ratings[i]>ratings[i+1]:
                c[i] = max(c[i+1]+1, c[i])
            sum += c[i]
        return sum + c[-1]

class Solution(object):
    def hammingWeight(self, a):
        """
        :type n: int
        :rtype: int
        """
        t = 1
        res = 0
        for i in range(32):
            if t & a != 0: res+=1
            t = t << 1
        return res

print(Solution().hammingWeight(129))
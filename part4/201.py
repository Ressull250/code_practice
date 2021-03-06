class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        return n << count

print Solution().rangeBitwiseAnd(6,12)

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, a):
        t = 1
        res = 0
        for i in range(32):
            if t & a != 0:
                res += 1 << (31 - i)
            t = t << 1
        return res

print Solution().reverseBits(43261596)
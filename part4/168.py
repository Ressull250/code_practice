class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = ord('A')
        s = ''

        while n != 0:
            n -= 1
            t = n % 26
            n = n / 26
            s = str(chr(base+t)) + s

        return s

print(Solution().convertToTitle(701))


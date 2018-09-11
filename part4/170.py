class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = 0
        for i,c in enumerate(reversed(s)):
            t += pow(26, i)*(ord(c)-ord('A')+1)

        return t

print(Solution().titleToNumber("ZY"))

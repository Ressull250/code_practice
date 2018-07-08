class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2) or sorted(s1) != sorted(s2): return False
        if s1 == s2: return True
        if len(s1) < 3: return True

        for i in range(1,len(s1)):
            if self.isScramble(s1[0:i],s2[0:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[0:i],s2[len(s1)-i:]) and self.isScramble(s1[i:],s2[0:len(s1)-i]):
                return True
        return False

print(Solution().isScramble("abcde","caebd"))


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        table = [0 for _ in range(26)]
        for i in s:
            table[ord(i) - ord('a')] += 1
        for i in t:
            table[ord(i) - ord('a')] -= 1
            if table[ord(i) - ord('a')] < 0:
                return False
        return True
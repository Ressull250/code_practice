class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split()
        dict = {}
        if len(pattern) != len(strs): return False
        for i,p in enumerate(pattern):
            if p in dict:
                if dict[p] == strs[i]: continue
                return False
            elif strs[i] in dict.values():
                return False
            else:
                dict[p] = strs[i]
        return True


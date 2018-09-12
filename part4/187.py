class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        map = set()
        res = set()
        for i in range(len(s)-9):
            if s[i:i+10] in map:
                res.add(s[i:i+10])
            else:
                map.add(s[i:i+10])
        return list(res)

print Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
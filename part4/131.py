class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def bt(s, other, res):
            if ishuiwen(s):
                res.append(other+[s])
            for i in range(len(s)):
                if ishuiwen(s[0:i]):
                    bt(s[i:], other+[s[0:i]], res)
                # if ishuiwen(s[i:]):
                #     bt(s[0:i], other+[s[i:]], res)

        def ishuiwen(str):
            if not str: return False
            return str[::-1] == str

        res = []
        bt(s, [], res)
        return min(res[0])

print Solution().partition("abb")
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        list = [False for _ in range(n+1)]
        list[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if list[j] and s[j:i] in wordDict:
                    list[i] = True
                    break
        return list[n]
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def bt(min, max, s, path, res):
            for i in range(min, max + 1):
                if i<=len(s) and s[0:i] in wordDict:
                    if s[i:]:
                        bt(min, max, s[i:], path + s[0:i] + ' ', res)
                    else:
                        res.append(path + s[0:i])
                        return
        if not self.wordBreak1(s, wordDict): return []
        if not wordDict: return []
        maxlen = max(len(word) for word in wordDict)
        minlen = min(len(word) for word in wordDict)
        res = []
        bt(minlen,maxlen,s,"",res)
        return res

    def wordBreak1(self, s, wordDict):
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

print Solution().wordBreak("a",[])


class Solution:

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        strs = [0, 1, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        if digits == '': return []

        ret = ['']
        for c in digits:
            tmp = []
            for a in strs[int(c)]:
                for s in ret:
                    tmp.append(s+a)
            ret = tmp

        return ret

print(Solution().letterCombinations(''))
        
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = list()
        self.backtrack(ret, '', 0, 0, n)
        return ret

    def backtrack(self, list, str, open, close, max):

        if len(str) == 2*max:
            list.append(str)
            return

        if open < max:
            self.backtrack(list, str+'(', open+1, close, max)
        if close < open:
            self.backtrack(list, str+')', open, close+1, max)


print(Solution().generateParenthesis(1))
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(queens, t45, t135):
            if len(queens) == n:
                result.append(queens)
                return

            for i in range(n):
                j = len(queens)
                if i not in queens and i - j not in t45 and i + j not in t135:
                    dfs(queens + [i], t45 + [i - j], t135 + [i + j])

        result = []
        dfs([], [], [])
        return len(result)
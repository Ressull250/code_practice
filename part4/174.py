import sys
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n,m = len(dungeon), len(dungeon[0])
        # if n == m == 1: return -(dungeon[n-1][m-1])+1 if dungeon[n-1][m-1] < 0 else 1
        table = [[sys.maxsize for _ in range(m+1)] for _ in range(n+1)]
        table[n][m-1] = table[n-1][m] = 1
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                table[i][j] = -dungeon[i][j] + min(table[i+1][j], table[i][j+1])
                if table[i][j] <= 0: table[i][j] = 1

        return table[0][0]

print Solution().calculateMinimumHP([[-200]]
)
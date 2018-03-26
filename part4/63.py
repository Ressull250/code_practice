class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1: return 0
        count = [[0 for _ in range(n)] for _ in range(m)]
        count[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and obstacleGrid[i-1][j] == 0:
                    count[i][j] += count[i - 1][j]
                if j - 1 >= 0 and obstacleGrid[i][j-1] == 0:
                    count[i][j] += count[i][j - 1]

        return count[m-1][n-1]

print(Solution().uniquePathsWithObstacles([[1,0],[0,0]]))

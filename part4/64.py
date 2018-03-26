class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if i-1>=0 and j-1>=0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif j-1>=0:
                    grid[i][j] += grid[i][j-1]
                elif i-1>=0:
                    grid[i][j] += grid[i-1][j]

        return grid[m-1][n-1]

print(Solution().minPathSum([[]]))
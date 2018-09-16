class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def findAll(i, j):
            grid[i][j] = '0'
            if i+1 < m and grid[i+1][j] == '1':
                findAll(i+1, j)
            if j+1 < n and grid[i][j+1] == '1':
                findAll(i, j+1)
            if i-1 >= 0 and grid[i-1][j] == '1':
                findAll(i-1, j)
            if j-1 >=0 and grid[i][j-1] == '1':
                    findAll(i, j-1)

        if not grid: return 0
        res = 0
        n,m = len(grid[0]), len(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0': continue
                findAll(i, j)
                res += 1
        return res

print Solution().numIslands([])


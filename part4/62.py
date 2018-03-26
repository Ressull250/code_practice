class Solution1(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [0]
        self.backtrak(m, n, 0, 0, count)
        return count[0]

    def backtrak(self, m, n, x, y, count):
        if x == m-1 and y == n-1:
            count[0]+=1
            return

        if x+1 < m:
            self.backtrak(m,n,x+1,y,count)
        if y+1 < n:
            self.backtrak(m,n,x,y+1,count)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [[0 for _ in range(n)] for _ in range(m)]
        count[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i-1>=0:
                    count[i][j] += count[i-1][j]
                if j-1>=0:
                    count[i][j] += count[i][j-1]

        return count[m-1][n-1]


print(Solution().uniquePaths(10,10))
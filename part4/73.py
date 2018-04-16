class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        c0,r0 = False,False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                    if i==0: c0 = True
                    if j==0: r0 = True

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if c0:
            for i in range(n): matrix[0][i] = 0
        if r0:
            for j in range(m): matrix[j][0] = 0

        return 0;

Solution().setZeroes([[1,0,3]])



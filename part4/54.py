class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []

        rmin,rmax,cmin,cmax = 0,len(matrix),0,len(matrix[0])
        res = []

        while rmin<rmax and cmin<cmax:
            for i in range(cmin,cmax): res.append(matrix[rmin][i])
            rmin += 1

            for i in range(rmin,rmax): res.append(matrix[i][cmax-1])
            cmax -= 1

            if rmin>=rmax or cmin>=cmax: break

            for i in range(cmin,cmax)[::-1]: res.append(matrix[rmax-1][i])
            rmax -= 1

            for i in range(rmin,rmax)[::-1]: res.append(matrix[i][cmin])
            cmin += 1

        return res

print Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])






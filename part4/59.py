class Solution(object):
    def generateMatrix(self, n):
        if n == 0 : return []

        rmin,rmax,cmin,cmax = 0, n, 0, n
        res,j = [[0 for _ in range(n)]for _ in range(n)],1

        while j <= n*n:
            for i in range(cmin,cmax): res[rmin][i] = j; j+=1
            rmin += 1

            for i in range(rmin,rmax): res[i][cmax-1] = j; j+=1
            cmax -= 1

            if rmin>=rmax or cmin>=cmax: break

            for i in range(cmin,cmax)[::-1]: res[rmax-1][i] = j; j+=1
            rmax -= 1

            for i in range(rmin,rmax)[::-1]: res[i][cmin] = j; j+=1
            cmin += 1

        return res

print(Solution().generateMatrix(1))
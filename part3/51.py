import copy
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = [['.' for _ in range(n)] for _ in range(n)]
        col = row = [False for _ in range(n)]
        ret = []

        self.tback(n, col.copy(), row.copy(), copy.deepcopy(ans), n, ret)
        return ret

    def tback(self, n, col, row, ans, left, ret):
        if left == 0:
            ret.append(copy.deepcopy(ans))
            return
        for i in range(n):
            if col[i]: continue
            for j in range(n):
                if row[j]:continue
                if not self.islegal(ans,i,j):continue
                ans[i][j] = 'Q'
                col[i] = row[j] = True
                self.tback(n,col,row,ans,left-1,ret)
                col[i] = row[j] = False
                ans[i][j] = '.'

    def islegal(self, ans, n, m):
        i,j = n,m
        while i+1<len(ans) and j+1<len(ans):
            if ans[i+1][j+1] == 'Q':return False
            else:
                i+=1;j+=1

        i,j = n,m
        while i-1>=0 and j-1>=0:
            if ans[i-1][j-1] == 'Q':return False
            else:
                i=i-1;j=j-1
        return True

print(Solution().solveNQueens(2))
# 自己的解法超时了，判断确实很僵硬
# 评论区有个思路我类似但是判断有优化的解法，见solution2
# solution3的大体思路是相同的，实现更妙一些
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        ans = [['.' for _ in range(n)] for _ in range(n)]
        ret = []

        self.tback(n, ans, n, ret, -1)
        return ret

    def tback(self, n, ans, left, ret, num):
        if left == 0:
            tmp = ["" for _ in range(n)]
            for i in range(n):
                t = ''
                for j in ans[i]:
                    t+=j
                tmp[i] = t
            ret.append(tmp)
            return
        for i in range(n):
            for j in range(n):
                if i*n+j <= num:continue
                if not self.islegal(ans,i,j): continue
                ans[i][j] = 'Q'
                self.tback(n,ans,left-1,ret,i*n+j)
                ans[i][j] = '.'
        return

    def islegal(self, ans, n, m):
        l,j = n,m
        while l+1<len(ans) and j+1<len(ans):
            if ans[l+1][j+1] == 'Q':return False
            else:
                l+=1;j+=1

        l,j = n,m
        while l-1>=0 and j-1>=0:
            if ans[l-1][j-1] == 'Q':return False
            else:
                l=l-1;j=j-1

        l, j = n, m
        while l+1<len(ans) and j-1>=0:
            if ans[l+1][j-1] == 'Q':return False
            l=l+1;j=j-1

        l, j = n, m
        while l-1>=0 and j + 1 <len(ans):
            if ans[l - 1][j + 1] == 'Q': return False
            l = l - 1;
            j = j + 1

        l, j = n, m
        while l+1<len(ans):
            if ans[l+1][j] == 'Q':return False
            l+=1

        l = n
        while l-1>=0:
            if ans[l-1][j] == 'Q':return False
            l-=1

        l, j = n, m
        while j+1<len(ans):
            if ans[l][j+1] == 'Q':return False
            j+=1

        j = m
        while j - 1 >=0:
            if ans[l][j - 1] == 'Q': return False
            j -= 1

        return True

class Solution2:
    def solveNQueens(self, n):

        ans,ret = [['.' for _ in range(n)] for _ in range(n)],[]
        self.tback(ans, 0, ret)
        return ret

    def tback(self, ans, col, ret):
        n = len(ans)
        if col==len(ans):
            tmp = ["" for _ in range(n)]
            for i in range(n):
                tmp[i] = ''.join(ans[i])
            ret.append(tmp)
            return
        for i in range(n):
            if self.isvalid(ans,i,col):
                ans[i][col] = 'Q'
                self.tback(ans, col+1, ret)
                ans[i][col] = '.'
        return

    def isvalid(self,ans,x,y):
        for i in range(len(ans)):
            for j in range(0,y):
                #分别对应 与ans[i][j]成45度，135度角，水平成直线的点
                if ans[i][j] == 'Q' and (x+y==i+j or x+j==y+i or x==i):
                    return False
        return True

    def solveNQueens3(self, n):
        def dfs(queens, t45, t135):
            if len(queens) == n:
                result.append(queens)
                return

            for i in range(n):
                j = len(queens)
                if i not in queens and i-j not in t45 and i+j not in t135:
                    dfs(queens+[i],t45+[i-j],t135+[i+j])

        result = []
        dfs([],[],[])
        return len(result)

print(Solution2().solveNQueens3(1))
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1,numRows+1):
            ans = [1 for _ in range(i)]
            for j in range(1,i-1):
                ans[j] = res[i-2][j-1] + res[i-2][j]
            res.append(ans)
        return res

print(Solution().generate(0))


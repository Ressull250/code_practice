class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m,n = len(matrix),len(matrix[0])
        l,r = 0,m*n-1
        while l<=r:
            mid = l + (r-l)/2
            val = matrix[mid//n][mid%n]
            if val > target:
                r = mid-1
            elif val < target:
                l = mid+1
            else:
                return True
        return False

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],13))
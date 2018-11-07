class Solution(object):
    def searchMatrix(self, matrix, target):

        if not matrix or not matrix[0]: return False

        x, y = 0, len(matrix[0])-1
        while x < len(matrix) and y >= 0:
            cur = matrix[x][y]
            if cur > target:
                y -= 1
            elif cur < target:
                x += 1
            else:
                return True
        return False


print Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
20)
# print Solution().bisearch([1,2,3,4,6],7)


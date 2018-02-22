class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        strs = set()
        for i,row in enumerate(board):
            for j,ele in enumerate(row):
                if ele != '.':
                    if ele + 'row' + str(i) not in strs:
                        strs.add(ele + 'row' + str(i))
                    else:
                        return False
                    if ele + 'col' + str(j) not in strs:
                        strs.add(ele + 'col' + str(j))
                    else:
                        return False
                    if ele + 'block' + str(i//3) + str(j//3) not in strs:
                        strs.add(ele + 'block' + str(i//3) + str(j//3))
                    else:
                        return False
        return True

board = [['1'],[],[],[],[],[]]
print(Solution().isValidSudoku(board))
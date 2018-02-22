class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.trackback(board)
        print(board)

    def trackback(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1,10):
                        if self.isValidSudoku(board,i,j,str(k)):
                            board[i][j] = str(k)
                            if self.trackback(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isValidSudoku(self, board, i, j, ele):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for k in range(9):
            if board[i][k]!='.' and board[i][k] == ele: return False
            if board[k][j]!='.' and board[k][j] == ele: return False
            if board[i//3*3+k//3][j//3*3+k%3]!='.' and \
                    board[i//3*3+k//3][j//3*3+k%3] == ele: return False
        return True


board = [["1","2","3","4","5","6","7","8","9"],[".",".",".",".",".",".",".",".","."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],[".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", ".", ".", "."]]
Solution().solveSudoku(board)
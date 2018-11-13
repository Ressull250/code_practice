class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                num = self.count(i, j, m, n, board)
                # die
                if num<2 or num>3:
                    continue
                # live or comeback
                if num == 3:
                    board[i][j] |= 2
                elif num == 2:
                    if board[i][j]:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        print board
    def count(self, i, j, m, n, board):
        num = 0
        for x in range(max(0, i-1), min(m, i+2)):
            for y in range(max(0, j-1), min(n, j+2)):
                num += board[x][y] & 1

        num -= board[i][j] & 1
        return num

Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
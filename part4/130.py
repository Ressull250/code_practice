class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def bfs(board, queue, path):

            tag = False
            while queue:
                r = queue.pop(0)
                c = queue.pop(0)
                rows, cols = len(board), len(board[0])
                if r == 0 or c==0 or r == rows-1 or c == cols-1:
                    tag = True

                if r+1 < rows and board[r+1][c] == 'O' and not visited[r+1][c]:
                    visited[r+1][c] = True
                    queue += [r+1,c]
                    path += [r+1,c]
                if c+1 < cols and board[r][c+1] == 'O' and not visited[r][c+1]:
                    visited[r][c+1] = True
                    queue += [r,c+1]
                    path += [r,c+1]
                if r-1 >= 0 and board[r-1][c] == 'O' and not visited[r-1][c]:
                    visited[r-1][c] = True
                    queue += [r-1,c]
                    path += [r-1,c]
                if c-1 >= 0 and board[r][c-1] == 'O' and not visited[r][c-1]:
                    visited[r][c-1] = True
                    queue += [r,c-1]
                    path += [r,c-1]

            if not tag:
                print(path)
                for i in range(len(path) / 2):
                    board[path[2 * i]][path[2 * i + 1]] = 'X'

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' and not visited[row][col]:
                    visited[row][col] = True
                    bfs(board, [row,col], [row,col])

Solution().solve([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]])
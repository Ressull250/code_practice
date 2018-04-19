# -*- coding:utf-8 -*-
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False
        if not word: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.trackback(board,word,i,j):
                    return True
        return False

    def trackback(self, board, word, x, y):
        if not word:
            return True
        #不能重复走
        if x<0 or y<0 or x>=len(board) or y>=len(board[0]) or word[0]!=board[x][y]:
            return False
        tmp = board[x][y]
        board[x][y] = ""
        res = self.trackback(board,word[1:],x+1,y) or self.trackback(board,word[1:],x-1,y) \
                or self.trackback(board,word[1:],x,y+1) or self.trackback(board,word[1:],x,y-1)
        board[x][y] = tmp
        return res

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCE"))
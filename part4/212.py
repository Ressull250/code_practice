class Node:
    def __init__(self, val):
        self.val = val
        self.nexts = []
        self.count = 0

class Trie:

    def __init__(self):
        self.root = Node(-1)

    def insert(self, word):
        n = self.root
        for i in word:
            for j in n.nexts:
                if i == j.val:
                    n = j
                    break
            else:
                t = Node(i)
                n.nexts.append(t)
                n = t
        n.count += 1

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def check(root, i, j, path):
            c = board[i][j]
            for t in root.nexts:
                if c == t.val:
                    tmpboard = board[i][j]
                    board[i][j] = ''
                    dfs(t, i, j, path+[t.val])
                    board[i][j] = tmpboard
                    if t.count > 0:
                        res.add("".join(path+[t.val]))
                    return

        def dfs(root, i, j, path):
            if i-1 >= 0:
                check(root, i-1, j, path)
            if j-1 >= 0:
                check(root, i, j-1, path)
            if i+1 < m:
                check(root, i+1, j, path)
            if j+1 < n:
                check(root, i, j+1, path)

        # initial trie tree
        tree = Trie()
        for w in words:
            tree.insert(w)

        res = set()
        m,n = len(board),len(board[0])

        for x in range(m):
            for y in range(n):
                check(tree.root, x, y, [])
        return list(res)





class Node:
    def __init__(self, val):
        self.val = val
        self.nexts = []
        self.count = 0

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(-1)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
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

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        def dfs(root, word):
            if not root: return False
            if not word and root.count > 0: return True
            if not word: return False
            target = word[0]
            flag = False
            if target == '.':
                for m in root.nexts:
                    flag = flag or dfs(m, word[1:])
                return flag
            else:
                for n in root.nexts:
                    if target == n.val:
                        return dfs(n, word[1:])
                else:
                    return False

        return dfs(self.root, word)

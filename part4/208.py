class Node:
    def __init__(self, val):
        self.val = val
        self.nexts = []
        self.count = 0


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(-1)

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        n = self.root
        for i in word:
            for j in n.nexts:
                if i == j.val:
                    n = j
                    break
            else:
                return False

        if n.count == 0:
            return False
        else:
            return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        n = self.root
        for i in prefix:
            for j in n.nexts:
                if i == j.val:
                    n = j
                    break
            else:
                return False
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert("ab")
obj.insert("a")
obj.insert("b")
print obj.search("b")

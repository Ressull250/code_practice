import copy
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList1 = copy.copy(wordList)
        dis = self.ladderLength(beginWord, endWord, wordList1)
        def find(path, begin, searched, res):
            if path>dis: return
            if begin == endWord:
                res.append(searched)
            for word in wordList:
                if word in searched:
                    continue
                else:
                    if word == begin:
                        continue
                    elif trans(begin, word):
                        find(path+1, word, searched+[word], res)

        def trans(word1, word2):
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    continue
                else:
                    return word1[i+1:] == word2[i+1:]
        res = []
        find(1, beginWord, [beginWord], res)
        return res

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def trans(word1, word2):
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    continue
                else:
                    return word1[i+1:] == word2[i+1:]
            return False

        queue = [beginWord]
        res = 2
        while queue:
            for i in range(len(queue)):
                word = queue.pop(0)
                j=0
                while j<len(wordList):
                    w = wordList[j]
                    if trans(w,word):
                        if w == endWord: return res
                        queue.append(w)
                        wordList.remove(w)
                    else:
                        j+=1
            res += 1
        return 0

# print(Solution().findLadders("a",
# "b",
# ["a","b","c"]))
print(Solution().findLadders("hit",
"cog",
["hot","dot","dog","lot","log","cog"]))
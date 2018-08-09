import sys
class Solution0(object):
    minpath = sys.maxsize
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def find(path, begin, searched):
            if begin == endWord:
                self.minpath = min(self.minpath, path)
            for word in wordList:
                if word in searched:
                    continue
                else:
                    if word == begin:
                        continue
                    elif trans(begin, word):
                        find(path+1, word, searched+[word])

        def trans(word1, word2):
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    continue
                else:
                    return word1[i+1:] == word2[i+1:]

        find(1, beginWord, [])
        return self.minpath if self.minpath != sys.maxsize else 0

class Solution1(object):
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

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # def trans(word, wordList, queue):
        #     l = [word[:index]+ch+word[index+1:]
        #          for index in range(word) for ch in 'abcdefghijklmnopqrstuvwxyz']
        #     for i in l:
        #         if i == endWord: return res
        #         if i in wordList:
        #             wordList.remove(l)
        #             queue.append(l)

        queue = [beginWord]
        res = 2
        while queue:
            for i in range(len(queue)):
                word = queue.pop(0)
                l = [word[:index] + ch + word[index + 1:]
                     for index in range(len(word)) for ch in 'abcdefghijklmnopqrstuvwxyz']
                for w in l:
                    if w in wordList:
                        if w == endWord: return res
                        wordList.remove(w)
                        queue.append(w)
            res += 1
        return 0
print(Solution().ladderLength("a",
"b",
["a","b","c"]))


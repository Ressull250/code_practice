class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0: return []
        num = len(words[0]); size = len(words); nums = []
        wordsmap = dict()
        for i in range(size):
            if words[i] not in wordsmap:
                wordsmap[words[i]] = 0
            else:
                wordsmap[words[i]] += 1


        for i in range(len(s)-num*size+1):
            mymap = dict()
            for j in range(size):
                word = s[i+j*num:i+j*num+num]
                if word not in wordsmap:
                    break
                else:
                    if word in mymap:
                        mymap[word] += 1
                    else:
                        mymap[word] = 0

                    if mymap[word] > wordsmap[word]:
                        break

                if j == size-1:
                    nums.append(i)

        return nums
S = "abaababbaba"
L = ["ab","ba","ab","ba"]
print(Solution().findSubstring(S,
L))


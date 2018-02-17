class Solution:

    # 超时
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0: return []
        num = len(words[0])
        nums = list()
        for i in range(len(s)):
            self.cursive(s,num,words,words.copy(),0,nums)
        return nums

    def cursive(self,s,num,words,wordsmap,i,nums):
        # 从此处开始新的寻找

        # 继承前一次寻找
        if len(wordsmap) == 0:
            tmp = i-len(words)*num
            if tmp not in nums:
                nums.append(tmp)

        if i+num <= len(s) :
            word = s[i:i+num]
            if word in wordsmap:
                wordsmap.remove(word)
                self.cursive(s,num,words,wordsmap,i+num,nums)

            if word in words:
                wordsmap = words.copy()
                wordsmap.remove(word)
                self.cursive(s,num,words,wordsmap,i+num,nums)

print(Solution().findSubstring("aaaaaaaa",
["aa","aa","aa"]))


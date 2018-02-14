class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        mstr = ''
        for i in range(len(s)):
            tmp = self.findLogest(s,i,i)
            if len(tmp) > len(mstr):
                mstr = tmp
            tmp = self.findLogest(s,i,i+1)
            if len(tmp) > len(mstr):
                mstr = tmp

        return mstr

    def findLogest(self,s,i,j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1
        return s[i+1:j]

print(Solution().longestPalindrome('abcbaaaaaa'))
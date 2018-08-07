class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l,r = 0,len(s)-1
        while l<r:
            while l<len(s)-1 and not s[l].isalnum():
                l += 1

            while r>0 and not s[r].isalnum():
                r -= 1

            if l>r: return True
            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1

        return True

print(Solution().isPalindrome("AF"
))
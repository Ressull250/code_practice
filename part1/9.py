class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False

        y=int(x)
        i=0
        while y>0:
            i = i*10 + y%10
            y //= 10

        return i==x

print(Solution().isPalindrome(-5555))
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 2 or num == 3 or num == 5 or num == 1: return True
        if num == 0: return False
        while True:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            elif num == 1:
                return True
            else:
                return False

print Solution().isUgly(1000)
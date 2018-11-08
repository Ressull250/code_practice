class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = int(num)
        while num >= 10:
            t = num
            num = 0
            while t:
                num += t%10
                t /= 10
        return num


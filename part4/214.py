class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # KMP TABLE
        news = s + "%" + s[::-1]
        table = [0 for _ in range(len(news))]
        for i in range(1,len(news)):
            t = table[i-1]
            while t>0 and news[t]!=news[i]:
                t = table[t-1]
            if news[t] == news[i]:
                t += 1
            table[i] = t
        return s[table[-1]:][::-1]+s





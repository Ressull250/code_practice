class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if pow(2,31)-1 < x or x < -pow(2,31):
            return 0

        tmp = x
        if tmp<0:
            tmp = -tmp

        s = str(tmp)[::-1]

        while s!='0' and s[0] == '0':
            s = s[1:]

        if x<0:
            s = '-' + s

        if  -pow(2,31) > int(s) or int(s)> pow(2,31)-1 :
            return 0

        return int(s)


print(Solution().reverse(-1534236469))
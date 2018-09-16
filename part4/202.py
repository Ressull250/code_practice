class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def next(num):
            t,sum = [],0
            while num != 0:
                val = num % 10
                sum += val*val
                t.append(val)
                num /= 10
            if sum == 1:
                return True
            elif t in table:
                return False
            else:
                table.append(t)
                return next(sum)

        table = []
        return next(n)

print Solution().isHappy(19)

class Solution1(object):
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

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def next(num):
            sum = 0
            while num != 0:
                val = num % 10
                sum += val*val
                num /= 10
            return sum

        slow = fast = n
        while True:
            slow = next(slow)
            if slow == 1:
                return True
            fast = next(fast)
            fast = next(fast)
            if slow == fast:
                break

        return False

print Solution().isHappy(19)

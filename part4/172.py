class Solution1(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def count5(num):
            count = 0
            while num/5 != 0 and num%5 ==0:
                count+=1
                num /= 5
            return count

        zero = 0
        for i in range(1,(n/5)+1):
            zero += count5(i*5)

        return zero

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n/5 != 0:
            count += n/5
            n /= 5
        return count

print(Solution().trailingZeroes(1808548329))

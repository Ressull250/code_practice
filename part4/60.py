import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k=k-1
        nums = [n for n in range(1,n+1)]
        res = ""
        while n > 0:
            tmp = k // math.factorial(n - 1)
            res += str(nums[tmp])
            nums.remove(nums[tmp])
            k = k % math.factorial(n-1)
            n = n-1
        return res


print(Solution().getPermutation(2,2))
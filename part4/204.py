class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        primes = [True for _ in range(n)]
        for i in range(2, n):
            if primes[i]:
                count += 1
                for j in range(2,n):
                    if i*j < n:
                        primes[i*j] = False
                    else:
                        break
        return count
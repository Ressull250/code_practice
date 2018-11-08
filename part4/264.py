class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = [0 for _ in range(n)]
        t[0] = 1
        p2 = p3 = p5 = 0
        for i in range(1,n):
            t[i] = min(t[p2]*2, t[p3]*3, t[p5]*5)
            if t[i] == t[p2]*2: p2 += 1
            if t[i] == t[p3]*3: p3 += 1
            if t[i] == t[p5]*5: p5 += 1

        return t[n-1]

print Solution().nthUglyNumber(7)


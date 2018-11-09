def isBadVersion(version):
    if version <= 5:
        return False
    else:
        return True
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n
        while l <= r:
            mid = l + (r-l)/2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

print Solution().firstBadVersion(0)
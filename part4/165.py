class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        for i in range(max(len(v1), len(v2))):
            t1 = int(v1[i]) if i < len(v1) else 0
            t2 = int(v2[i]) if i < len(v2) else 0
            if t1 > t2:
                return 1
            elif t1 < t2:
                return -1
        return 0


print Solution().compareVersion("2.0", "2")
print "01.1".split(".")
print(int("01"))
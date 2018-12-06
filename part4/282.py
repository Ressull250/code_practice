class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ret = []
        self.dps(num, 0, '', 0, target, ret, 0)
        return ret

    def dps(self, num, pos, path, val, target, ret, last):
        if pos == len(num):
            if val == target:
                ret.append(path)
            return

        for i in range(pos,len(num)):
            # deal with digits start with 0
            if num[pos] == '0' and i != pos:
                break

            s = num[pos:i+1]
            if pos == 0:
                self.dps(num, i+1, s, int(s), target, ret, int(s))
            else:
                self.dps(num, i+1, path + '+' + s, val + int(s), target, ret, int(s))
                self.dps(num, i+1, path + '-' + s, val - int(s), target, ret, -int(s))
                self.dps(num, i+1, path + '*' + s, (val-last) + (last*int(s)), target, ret, last*int(s))

print Solution().addOperators('123',6)
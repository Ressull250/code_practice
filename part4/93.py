class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.find(s, [], res)
        return res

    def find(self, s, this, res):
        if len(this) > 4:
            return
        if len(s) == 0 and len(this) == 4:
            str = this[0]+'.'+this[1]+'.'+this[2]+'.'+this[3]
            res.append(str)
            return
        for i in range(len(s)):
            if i >= 3:
                return
            if i >= 1 and s[0] == '0':
                return
            if int(s[0:i+1]) <= 255:
                self.find(s[i+1:], this+[s[0:i+1]], res)

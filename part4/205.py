class Solution0:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def count(ss):
            table,res = [],[]
            for i in ss:
                if i not in table:
                    table.append(i)
                res.append(table.index(i))
            return res
        t1 = count(s)
        t2 = count(t)
        return t1 == t2

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for i,j in zip(s,t):
            if i in dict:
                if dict[i] != j:
                    return False
            else:
                if j in dict.values():
                    return False
                dict[i] = j
        return True

print(Solution().isIsomorphic("",""))

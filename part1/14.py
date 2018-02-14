class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""

        prefix = strs[0]
        for s in strs:
            if s.startswith(prefix):
                continue
            elif s == '':
                prefix = ''
            else:
                out = -1;
                for i in range(len(prefix)):
                    if i >= len(s):
                        break
                    elif s[i] == prefix[i]:
                        out = i;
                    else:
                        break
                prefix = prefix[0:out+1]

        return prefix

print(Solution().longestCommonPrefix(['abb','abbc'])[-1:-2])

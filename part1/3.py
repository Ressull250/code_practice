
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr = ''; maxlen = 0;
        for i,t in enumerate(s):
            if t in substr:
                substr = substr[substr.index(t)+1:] + t
            else:
                substr += t
                if len(substr) > maxlen:
                    maxlen = len(substr)

        return maxlen

print(Solution().lengthOfLongestSubstring("abcabccc"))
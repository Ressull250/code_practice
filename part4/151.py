class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = s.split(" ")
        list.reverse()
        if list and list[0] == "":
            list.pop(0)
        if list and list[-1] == "":
            list.pop(-1)
        print(list)
        a = " ".join(s.strip().split()[::-1])
        b = " ".join(list)
        return " ".join(list)
        # return " ".join(s.strip().split()[::-1])

print(Solution().reverseWords("    "))
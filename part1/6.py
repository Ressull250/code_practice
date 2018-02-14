class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        nums = list()
        for i in range(numRows):
            nums.append('')

        i = 0
        while i<len(s):
            for j in range(numRows):
                if i<len(s):
                    nums[j] += s[i]
                i += 1

            for j in range(numRows-2):
                if i<len(s):
                    nums[numRows-2-j] += s[i]
                i += 1


        retstr = ''
        for i in range(numRows):
            retstr += nums[i]

        return retstr

print(Solution().convert("PAYPALISHIRING", 3))
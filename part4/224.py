class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = sum = 0
        sign = 1
        stack = []
        for i in s:
            if i == ' ':
                continue
            elif i == '+':
                sum += sign*num
                sign = 1
                num = 0
            elif i == '-':
                sum += sign * num
                sign = -1
                num = 0
            elif i == '(':
                stack.append(sum)
                stack.append(sign)
                sum = 0
                sign = 1
            elif i == ')':
                sum += sign*num
                sum = stack.pop(-1)*sum + stack.pop(-1)
                num = 0
                sign = 1
            else:
                num = num*10 + ord(i) - ord('0')
        sum += sign * num

        return sum

print Solution().calculate("0-(3+5)-500")

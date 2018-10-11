class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = '+'
        for i in s:
            if i == ' ' :
                continue
            if i.isdigit():
                num = num * 10 + ord(i) - ord('0')
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    t = stack.pop()
                    stack.append(t/num if t>0 else -((-t)/num))
                sign = i
                num = 0
        else:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                t = stack.pop()
                stack.append(t/num if t>0 else -((-t)/num))

        return sum(stack)
print(Solution().calculate("14-3/2"))
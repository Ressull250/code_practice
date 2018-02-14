import queue

class Solution:
    def isValid(self, s):
        stack = queue.LifoQueue()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.put(c)
            else:
                if stack.empty(): return False
                g = stack.get()
                if (g=='(' and c==')') or (g=='{' and c=='}') or (g=='[' and c==']'):
                    continue
                else:
                    return False

        if stack.empty():
            return True
        else:
            return False

print(Solution().isValid(']'))


import queue
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = queue.LifoQueue()
        maxlen = 0
        stk.put(-1)
        for i,c in enumerate(s):
            if c == '(':
                stk.put(i)
            elif c == ')':
                stk.get()
                if stk.empty():
                    stk.put(i)
                else:
                    t = stk.get()
                    maxlen = max(maxlen,i-t)
                    stk.put(t)

        return maxlen

print(Solution().longestValidParentheses('(())))'))

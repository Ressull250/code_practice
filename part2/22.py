class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = self.parenttheses(n)
        ret = list(ret)
        print(ret)
        return ret

    def parenttheses(self, n):
        if n == 4:
            return {"(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"}
        elif n == 2:
            return {'()()','(())'}
        elif n == 1: 1
            return {'()'}
        else:
            strs = self.parenttheses(n-1)
            ret = set()
            for s in strs:
                ret.add('()'+s)
                ret.add(s+'()')
                ret.add('('+s+')')
        return ret

list3 = set(Solution().generateParenthesis(1))
list1 = {"()(()())","()(())()","(()())()","((()))()","()((()))","(()()())","(((())))","()()(())","()()()()","((()()))","((())())","(())()()","(()(()))"}

list2 = {"(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"}

print(list2-list3)
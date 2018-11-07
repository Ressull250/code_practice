class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        for i,ch in enumerate(input):
            if ch in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[0:i])
                right = self.diffWaysToCompute(input[i+1:])
                for x in left:
                    for y in right:
                        if ch == '+':
                            res.append(x+y)
                        elif ch == '-':
                            res.append(x-y)
                        elif ch == '*':
                            res.append(x*y)
        if not res:
            return [int(input)]
        return res

print Solution().diffWaysToCompute("12")


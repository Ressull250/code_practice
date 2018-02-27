class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        c = 0
        ret = [0 for _ in range(len(num1)+len(num2))]
        for i in range(len(num1))[::-1]:
            for j in range(len(num2))[::-1]:
                sum = int(num1[i])*int(num2[j])
                sum += ret[i+j+1]

                ret[i+j] += sum // 10
                ret[i+j+1] = sum % 10

        s = ''
        for c in ret:
            if not s and c==0: continue
            s += str(c)

        return s if s else '0'

print(Solution().multiply('123','101'))
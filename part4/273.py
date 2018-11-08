class Solution(object):
    def numberToWords(self, num):
        to19 = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Zero Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        if num == 0: return 'Zero'

        def helper(t):
            if t == 0: return ''
            res = ''
            b = t / 100
            if b != 0:
                res += to19[b] + ' Hundred'
            b = t % 100
            if b == 0:
                pass
            elif b < 20:
                if res: res += ' ' + to19[b]
                else: res = to19[b]
            else:
                if res:
                    res += ' ' + tens[b/10]
                else:
                    res = tens[b/10]
                if b % 10 != 0:
                    res += ' ' + to19[b%10]
            return res

        s = ''
        if num/1000000000 != 0:
            s += helper(num/1000000000) + ' Billion'
            num %= 1000000000

        if num/1000000 != 0:
            if s: s += ' '
            s += helper(num/1000000) + ' Million'
            num %= 1000000

        if num/1000 != 0:
            if s: s += ' '
            s += helper(num/1000) +' Thousand'

        if s: s += ' '
        s+= helper(num%1000)

        if s.endswith(' '):
            return s[0:len(s)-1]
        return s

print Solution().numberToWords(1000)





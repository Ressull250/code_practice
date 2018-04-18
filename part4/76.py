# -*- coding:utf-8 -*-
import sys
class Solution:
    def minWindow(self, s, t):
        map = [0 for _ in range(128)]
        begin,end,minbegin,minlen = 0,0,0,sys.maxsize
        counter = len(t)

        # 初始化map
        for c in t:
            map[ord(c)]+=1

        while end<len(s):
            # 改变条件
            if map[ord(s[end])] > 0:
                counter-=1
            map[ord(s[end])]-=1
            end+=1

            while counter == 0:
                # 判断是否是最小
                if end-begin<minlen:
                    minlen = end-begin
                    minbegin = begin

                # 移动begin
                map[ord(s[begin])]+=1
                if map[ord(s[begin])]>0:
                    counter+=1
                begin+=1

        if minlen == sys.maxsize:
            return ""
        return s[minbegin:minbegin+minlen]

print Solution().minWindow("a","abcd")


# -*- coding:utf-8 -*-
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []

        # 评论区的思路，开始用的是comp，用key会快很多
        # def comp(a, b):
        #     if a.start == b.start:
        #         flag = a.end > b.end
        #     else:
        #         flag = a.start > b.start
        #     if flag: return 1;
        #     return -1

        intervals.sort(key=lambda x:x.start)
        res = [intervals[0]]

        for i in intervals:
            last = res[-1]
            if last.end >= i.start: res[-1] = Interval(last.start,i.end if i.end>last.end else last.end)
            else: res.append(i)

        return res



print Solution().merge([Interval(1,4),Interval(2,3)])
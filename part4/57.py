# -*- coding:utf-8 -*-
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals: return [newInterval]

        for i,inter in enumerate(intervals):
            if newInterval.start<inter.start:
                intervals.insert(i,newInterval)
                break
            if i == len(intervals)-1:
                intervals.append(newInterval)
                break

        # 抄的56题的
        res = [intervals[0]]

        for i in intervals:
            last = res[-1]
            if last.end >= i.start:
                res[-1] = Interval(last.start, i.end if i.end > last.end else last.end)
            else:
                res.append(i)

        return res

print(Solution().insert([Interval(1,5)],Interval(2,3)))
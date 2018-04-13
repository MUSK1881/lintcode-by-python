# -*- coding: utf-8 -*-
"""
给出若干闭合区间，合并所有重叠的部分。

样例
Given intervals => merged intervals:

[                     [
  (1, 3),               (1, 6),
  (2, 6),      =>       (8, 10),
  (8, 10),              (15, 18)
  (15, 18)            ]
]
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if intervals == []:
            return []
        
        intervals = sorted(intervals, key=lambda x: x.start)
        
        res = []
        res.append(intervals[0])
        for i in intervals:
            if i.start > res[-1].end:
                res.append(i)
            else:
                res[-1].end = max(i.end, res[-1].end)
        return res
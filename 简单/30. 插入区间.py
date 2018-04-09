# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 09:49:13 2018

@author: lenovo
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
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        results = []  
        insertindex = 0  
        for interval in intervals:  
            if interval.end < newInterval.start:  
                results.append(interval)  
                insertindex += 1  
            elif interval.start > newInterval.end:  
                results.append(interval)  
            else:  
                newInterval.start = min(interval.start, newInterval.start)  
                newInterval.end = max(interval.end, newInterval.end)  
        results.insert(insertindex, newInterval)  
        return results  
            
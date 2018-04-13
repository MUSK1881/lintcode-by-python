# -*- coding: utf-8 -*-
"""
给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。

你可以假设在数组中无重复元素。

样例
[1,3,5,6]，5 → 2

[1,3,5,6]，2 → 1

[1,3,5,6]， 7 → 4

[1,3,5,6]，0 → 0
"""

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A == [] or min(A) > target :
            return 0
        
        if max(A) < target:
            return len(A)
            
        for i in range(len(A)):
            if A[i] == target:
                return i
            else:
                if A[i] < target and A[i+1] > target :
                    return i+1
            
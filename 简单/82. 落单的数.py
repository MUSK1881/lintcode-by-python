# -*- coding: utf-8 -*-
"""
给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

样例
给出 [1,2,2,1,3,4,3]，返回 4
"""

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        if len(A) == 1:
            return(A[0])
        A = sorted(A)
        for i in range(0,len(A),2):
            if i == len(A)-1:
                return(A[-1])
            if A[i] != A[i+1]:
                return A[i]
            
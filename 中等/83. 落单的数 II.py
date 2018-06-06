# -*- coding: utf-8 -*-
"""
给出3*n + 1 个的数字，除其中一个数字之外其他每个数字均出现三次，找到这个数字。

样例
给出 [1,1,2,3,3,3,2,2,4,1] ，返回 4

挑战
一次遍历，常数级的额外空间复杂度
"""

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        # write your code here
        A.sort()
        i = 2
        while i < len(A):
            if A[i-2] != A[i]:
                return A[i-2]
            i += 3
        return A[-1]
                
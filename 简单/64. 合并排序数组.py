# -*- coding: utf-8 -*-
"""
合并两个排序的整数数组A和B变成一个新的数组。

样例
给出 A = [1, 2, 3, empty, empty], B = [4, 5]

合并之后 A 将变成 [1,2,3,4,5]
"""

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for i in range(n):
            A[i+m] = B[i]
        A.sort()
        return A
# -*- coding: utf-8 -*-
"""
实现 int sqrt(int x) 函数，计算并返回 x 的平方根。

样例
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3
"""

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(int(x/2)+1):
            if i ** 2 <= x and (i + 1) ** 2 > x:
                return i
# -*- coding: utf-8 -*-
"""
有一个机器人的位于一个 m × n 个网格左上角。

机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。

问有多少条不同的路径？

样例
给出 m = 3 和 n = 3, 返回 6.
给出 m = 4 和 n = 5, 返回 35
"""

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m == 1 or n == 1:
            return 1
            
        mn = []
        for i in range(m):
            tmps = []
            for j in range(n):
                if i == 0 or j == 0:
                    tmps.append(1)
                else:
                    tmps.append(0)
            mn.append(tmps)
            
        for i in range(1,m):
            for j in range(1,n):
                mn[i][j] = mn[i-1][j] + mn[i][j-1]
        
        return mn[m-1][n-1]
# -*- coding: utf-8 -*-
"""
给定一个只含非负整数的m*n网格，找到一条从左上角到右下角的可以使数字和最小的路径。
"""

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])  
        for i in range(m):  
            for j in range(n):  
                if i==0 and j==0:  
                    continue
                if i==0 and j!=0:  
                    grid[i][j]=grid[i][j-1]+grid[i][j]          
                if i!=0 and j==0:  
                    grid[i][j]=grid[i-1][j]+grid[i][j]  
                if i!=0 and j!=0:  
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]  
        return grid[m-1][n-1]
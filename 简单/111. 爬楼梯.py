# -*- coding: utf-8 -*-
"""
假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

样例
比如n=3，1+1+1=1+2=2+1=3，共有3种不同的方法

返回 3
"""

def climbStairs(n):
    # write your code here
    if n == 0 or n == 1:
        return 1
    res = [1,2]
    for i in range(2,n):
        res.append(res[i-2] + res[i-1])
            
    return res[n-1]
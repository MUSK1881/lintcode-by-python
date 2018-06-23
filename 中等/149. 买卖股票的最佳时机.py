'''
假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。如果你最多只允许完成一次交易(例如,一次买卖股票),设计一个算法来找出最大利润。

样例
给出一个数组样例 [3,2,3,1,2], 返回 1 
'''
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        res = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        
        m = 0
        r = 0
        for i in range(len(prices)-1):
            m = m + res[i]
            if m < 0:
                m = 0
            elif m > r:
                r = m
        return r
        

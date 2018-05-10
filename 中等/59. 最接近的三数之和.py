# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:17:03 2018

@author: lenovo
"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        res = numbers[0] + numbers[1] + numbers[2]
        for i in range(len(numbers) - 2):
            j = i + 1
            k = len(numbers) - 1
            while j < k:
                Sum = numbers[i] + numbers[j] + numbers[k] 
                if Sum == target:
                    return target
                if abs(Sum - target) < abs(res - target):
                    res = Sum
                if Sum > target:
                    k -= 1
                if Sum < target:
                    j += 1
        return res
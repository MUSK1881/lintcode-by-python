# -*- coding: utf-8 -*-
"""
跟进“删除重复数字”：

如果可以允许出现两次重复将如何处理？
"""

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if nums == []:
            return 0
        
        c = 0
        times = 1
        for i in range(1,len(nums)):
            if nums[c] != nums[i]:
                c += 1
                times = 1
                nums[c] = nums[i]
            else:
                if times >= 2:  
                    continue  
                else:  
                    c += 1  
                    nums[c] = nums[i]  
                    times += 1 
        return c + 1
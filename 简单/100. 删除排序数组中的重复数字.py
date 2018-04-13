# -*- coding: utf-8 -*-
"""
给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。

不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。

样例
给出数组A =[1,1,2]，你的函数应该返回长度2，此时A=[1,2]。
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
       
        for i in range(1,len(nums)):
            if nums[c] != nums[i]:
                c += 1
                nums[c] = nums[i]
            else:
                
        return c + 1
        
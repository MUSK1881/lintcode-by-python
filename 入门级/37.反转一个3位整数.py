# -*- coding: utf-8 -*-
"""
37. 反转一个3位整数

反转一个只有3位数的整数。

样例
123 反转之后是 321。
900 反转之后是 9。
"""

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        
        return int(str(number)[::-1])
        
     

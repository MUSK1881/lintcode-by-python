# -*- coding: utf-8 -*-
"""
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

样例
如果 source = "source" 和 target = "target"，返回 -1。

如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。

"""

class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        if source == None or target == None:
            return -1
            
        l_s = (len(source))
        l_t = (len(target))
        
        if l_t == 0 or source == target:
            return 0
        
        for i in range(l_s-l_t+1):
            if source[i:i+l_t] == target:
                return i
        return -1 
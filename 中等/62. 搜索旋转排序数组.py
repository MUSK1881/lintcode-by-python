# -*- coding: utf-8 -*-
"""
Created on Thu May 10 21:55:34 2018

@author: lenovo
"""

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A == []:
            return -1
        for i in range(len(A)):
            print(i,A[i])
            if A[i] == target:
                return i
            else:
                return -1
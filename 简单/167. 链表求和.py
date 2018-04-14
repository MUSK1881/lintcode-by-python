# -*- coding: utf-8 -*-
"""
你有两个用链表代表的整数，其中每个节点包含一个数字。
数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
写出一个函数将两个整数相加，用链表形式返回和。

样例
给出两个链表 3->1->5->null 和 5->9->2->null，返回 8->0->8->null
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        if not l1:
            return l2
        if not l2:
            return l1
        
        # h1 和 h2 是两个指针
        h1 = l1
        h2 = l2
        
        while h1.next or h2.next:
            if not h1.next:
                h1.next = ListNode(0)
            if not h2.next:
                h2.next = ListNode(0)
            
            sumnum = h1.val + h2.val
            if sumnum >= 10:
                h1.val = sumnum%10
                h1.next.val += 1
            else:
                h1.val = sumnum
            h1 = h1.next
            h2 = h2.next
        
        h1.val = h1.val + h2.val
        if h1.val >= 10:
            h1.val = h1.val%10
            h1.next = ListNode(1)
        return l1
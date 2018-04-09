# -*- coding: utf-8 -*-
"""
翻转一个链表

样例
给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null
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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        # 用循环
        
        if head is None or head.next is None:
            return head
        
        # pre 和 cur 两个指针
        cur = head
        pre = None
        tmp = None
        
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            
        return pre
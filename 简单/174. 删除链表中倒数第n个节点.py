# -*- coding: utf-8 -*-
"""
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。

样例
给出链表1->2->3->4->5->null和 n = 2.

删除倒数第二个节点之后，这个链表将变成1->2->3->5->null.
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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        
        l1 = head
        l = 1
        while l1.next:
            l1 = l1.next
            l += 1
        l2 = l - n 
        if l2 == 0:
            return head.next
        cur = head
        pre = head
        while l2 > 0:
            pre = cur
            cur = cur.next
            l2 -= 1
        pre.next = cur.next
        return head
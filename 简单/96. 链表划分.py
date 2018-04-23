# -*- coding: utf-8 -*-
"""
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。

你应该保留两部分内链表节点原有的相对顺序。

样例
给定链表 1->4->3->2->5->2->null，并且 x=3

返回 1->2->2->4->3->5->null
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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if not head:
            return None
        l1 = ListNode(0)
        l2 = ListNode(0)
        h1 = l1
        h2 = l2
        cur = head
        while cur:
            if cur.val < x:
                l1.next = cur
                l1 = l1.next
            else:
                l2.next = cur
                l2 = l2.next
            cur = cur.next
        l2.next = None
        l1.next = h2.next
        return h1.next
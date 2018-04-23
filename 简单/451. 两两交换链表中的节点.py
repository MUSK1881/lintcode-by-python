# -*- coding: utf-8 -*-
"""
给一个链表，两两交换其中的节点，然后返回交换后的链表。

样例
给出 1->2->3->4, 你应该返回的链表是 2->1->4->3。
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
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        h = head
        while h and h.next:
            h.val, h.next.val = h.next.val, h.val
            h = h.next.next
        return head
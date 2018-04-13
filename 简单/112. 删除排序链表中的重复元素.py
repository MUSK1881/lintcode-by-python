# -*- coding: utf-8 -*-
"""
给定一个排序链表，删除所有重复的元素每个元素只留下一个

样例
给出 1->1->2->null，返回 1->2->null

给出 1->1->2->3->3->null，返回 1->2->3->null
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
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return None
        pre = head
        cur = head.next
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return head
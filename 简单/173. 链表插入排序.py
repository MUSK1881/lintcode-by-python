# -*- coding: utf-8 -*-
"""
用插入排序对链表排序

样例
Given 1->3->2->0->null, return 0->1->2->3->null

AC 95%
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head
        # dummy是新的链表表头
        # p 和 cur 是两个指针
        dummy = ListNode(0)
        while cur:
            p = dummy
            while p.next and cur.val > p.next.val:
                p = p.next
            pNext = p.next
            curNext = cur.next
            # pNext 和 curNext 是 p.next 和 cur.next 的链表头 
            # 没有这两步，链表就断了
            p.next = cur
            cur.next = pNext
            cur = curNext
        return dummy.next
"""
删除链表中等于给定值val的所有节点。

样例
给出链表 1->2->3->3->4->5->3, 和 val = 3, 
你需要返回删除3之后的链表：1->2->4->5。
"""

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        pre = dummy
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next
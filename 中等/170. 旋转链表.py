'''
给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数

样例
给出链表1->2->3->4->5->null和k=2

返回4->5->1->2->3->null
'''
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if not head:
            return None
        
        cur = head
        count = 1 
        while cur.next:
            cur = cur.next
            count += 1 
        
        cur.next = head
        
        diff = count - k % count
        while diff > 1:
            head = head.next
            diff -= 1
            
        tmp = head.next
        head.next = None
        
        return tmp
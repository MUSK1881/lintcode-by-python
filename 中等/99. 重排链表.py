"""
描述
给定一个单链表L: L0→L1→…→Ln-1→Ln,

重新排列后为：L0→Ln→L1→Ln-1→L2→Ln-2→…

必须在不改变节点值的情况下进行原地操作。
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if not head or not head.next:
            return head
        
        # 找到中点
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        # 翻转列表
        cur = mid
        pre = None
        tmp = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            
        head1 = pre
        pre1 = head
        
        # 逐个插入
        while head1:
            tmp1 = head1.next
            head1.next = pre1.next
            tmp2 = pre1.next
            pre1.next = head1
            pre1 = tmp2
            head1 = tmp1
            
        while head:
            print(head.val)
            head = head.next
            
        return head

 
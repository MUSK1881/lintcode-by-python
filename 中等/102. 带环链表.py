'''
描述
给定一个链表，判断它是否有环。

样例
给出 -21->10->4->5, tail connects to node index 1，返回 true

挑战
不要使用额外的空间
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
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if not head: return False 
        fast = head 
        slow = head 
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False 
'''
合并k个排序链表，并且返回合并后的排序链表。尝试分析和描述其复杂度。

样例
给出3个排序链表[2->4->null,null,-1->null]，返回 -1->2->4->null
'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
# Methode1
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
                
        temp = ListNode(-1)
        head = temp
        while heap:
            smallestNode_val = heapq.heappop(heap)
            temp.next = ListNode(smallestNode_val)
            temp = temp.next
        
        return head.next
    

# Methode2
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = []
        for node in lists:
            while node:
                l.append(node.val)
                node = node.next
        l.sort()
        temp = ListNode(-1)
        head = temp
        for i in l:
            temp.next = ListNode(i)
            temp = temp.next
        
        return head.next
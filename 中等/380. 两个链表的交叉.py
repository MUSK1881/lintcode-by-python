'''
如果两个链表没有交叉，返回null。
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
'''
"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:  
    # @param headA: the first list  
    # @param headB: the second list  
    # @return: a ListNode  
    def getIntersectionNode(self, headA, headB):  
        curA, curB = headA, headB  
        countA, countB = 0, 0  
        # 两个循环，统计两个链表的长度  
        while curA:  
            countA += 1  
            curA = curA.next  
        while curB:  
            countB += 1  
            curB = curB.next  
        # 计算长度差  
        gap = abs(countA - countB)  
        # 令长的链表先走gap长  
        if countA >= countB:  
            while gap != 0:  
                headA = headA.next  
                gap -= 1  
        else:  
            while gap != 0:  
                headB = headB.next  
                gap -= 1  
        # 开始遍历，看是否能指向同一节点  
        curA, curB = headA, headB  
        while curA:  
            if curA == curB:  
                return curA  
            curA = curA.next  
            curB = curB.next  
        return None 
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:59:45 2018

@author: lenovo
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        # m 处打断
        if not head: return None
        
        a = 0
        cur = ListNode(0)
        cur.next = head
        while a < m-1 :
            cur = cur.next
            a += 1
        tmp1 = cur
        t1 = cur.next
        cur.next = None
        cur = t1
        
        # n 处打断
        diff = n-m
        b = 0
        while b < diff:
            cur = cur.next
            b += 1
            
        tmp2 = cur
        t2 = cur.next
        cur.next = None
        cur = t2 
        
        
        # mn 处翻转
        cur1 = t1 
        pre1 = None
        while cur1:
            tmp = cur1.next
            cur1.next = pre1
            pre1 = cur1
            cur1 = tmp
            
        while t1:
            print(t1.val)
            t1 = t1.next
            
        # 三块连接
        tmp1.next = tmp2
        t1.next = t2
        
        return head
    
a = [ListNode(i) for i in range(10)]

for i in range(9):
    a[i].next = a[i+1]

c = a[0]

s = Solution()
s.reverseBetween(c,1,5)
print(' ')
while c:
    print(c.val)
    c = c.next




    



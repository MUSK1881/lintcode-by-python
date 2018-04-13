# -*- coding: utf-8 -*-
"""
给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        results = []
        q = [root]
        
        if root is None:
            return []
            
        while q:
            q_new = []
            results.append([n.val for n in q])
            for node in q:
                if node.left:
                    q_new.append(node.left)
                if node.right:
                    q_new.append(node.right)
            q = q_new
        return results
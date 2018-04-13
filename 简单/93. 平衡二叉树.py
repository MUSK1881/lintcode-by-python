# -*- coding: utf-8 -*-
"""
给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。 

样例
给出二叉树 A={3,9,20,#,#,15,7}, B={3,#,20,15,7}

A)  3            B)    3 
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
二叉树A是高度平衡的二叉树，但是B不是
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
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def getdepth(self, Root):
        if not Root:
            return 0
        ldepth = self.getdepth(Root.left)
        rdepth = self.getdepth(Root.right)
        return max(ldepth, rdepth) + 1
    
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        ldepth = self.getdepth(root.left)
        rdepth = self.getdepth(root.right)
        
        if abs(ldepth-rdepth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
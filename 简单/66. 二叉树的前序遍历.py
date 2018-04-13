# -*- coding: utf-8 -*-
"""
给出一棵二叉树，返回其节点值的前序遍历。
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
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if root == None:
             return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
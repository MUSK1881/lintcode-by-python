# -*- coding: utf-8 -*-
"""
翻转一棵二叉树

样例
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        if root is None:  
            return None  
        root.left, root.right = self.invertBinaryTree(root.right), self.invertBinaryTree(root.left)
        return root

# -*- coding: utf-8 -*-
"""
在二叉树中寻找值最大的节点并返回。

样例
给出如下一棵二叉树：

     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5 
返回值为 3 的节点。
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
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        # write your code here
        if root is None:
            return None
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left, right))
        
    def max(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.val > b.val:
            return a
        return b
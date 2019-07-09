#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (32.83%)
# Likes:    1025
# Dislikes: 140
# Total Accepted:    127.2K
# Total Submissions: 367.5K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
# 
# Note: 
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level h.
# 
# Example:
# 
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# Output: 6
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # My solution - O(2^n)
    def countNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Most-voted
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.getDepthLeft(root)
        rightDepth = self.getDepthRight(root)
        return self.helper(root, leftDepth, rightDepth)

    def helper(self, root, leftDepth, rightDepth):
        if leftDepth == rightDepth:
            return pow(2, leftDepth) - 1
        else:
            return 1\
                    + self.helper(root.left, leftDepth - 1, self.getDepthRight(root.left))\
                    + self.helper(root.right, self.getDepthLeft(root.right), rightDepth - 1)
            
    def getDepthLeft(self, root):
        if not root:
            return 0
        return 1 + self.getDepthLeft(root.left)
    
    def getDepthRight(self, root):
        if not root:
            return 0
        return 1 + self.getDepthRight(root.right)
    

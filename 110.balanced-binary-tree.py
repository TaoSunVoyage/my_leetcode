#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (40.77%)
# Likes:    1231
# Dislikes: 109
# Total Accepted:    320.9K
# Total Submissions: 783.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # My solution
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: 
            return True
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))
        lDepth = depth(root.left)
        rDepth = depth(root.right)
        return abs(lDepth - rDepth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    # Most-voted solution
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        self.getHeight(root)
        return self.flag

    def getHeight(self, root):
        if not root: return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1:
            self.flag = False
        return 1 + max(left, right)
    
    # Most-voted solution 2
    def isBalanced(self, root: TreeNode) -> bool:
        return self.getHeight(root) != -1
    def getHeight(self, root):
        if not root: return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if left == -1 or right == -1: return -1
        if abs(left - right) > 1: return -1
        return 1 + max(left, right)



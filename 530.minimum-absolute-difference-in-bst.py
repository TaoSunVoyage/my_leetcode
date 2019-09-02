#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (50.19%)
# Likes:    592
# Dislikes: 42
# Total Accepted:    66.1K
# Total Submissions: 128.7K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
# 
# 
# 
# 
# Note: There are at least two nodes in this BST.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # My solution
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        if root.right:
            cur = root.right
            while cur.left:
                cur = cur.left
            minRight = cur.val - root.val
            rightMin = self.getMinimumDifference(root.right)
        else:
            minRight = float("inf")
            rightMin = float("inf")
        
        if root.left:
            cur = root.left
            while cur.right:
                cur = cur.right
            minLeft = root.val - cur.val
            leftMin = self.getMinimumDifference(root.left)
        else:
            minLeft = float("inf")
            leftMin = float("inf")
        
        return min(rightMin, leftMin, minRight, minLeft)

    # Most-voted
    def getMinimumDifference(self, root: TreeNode) -> int:
        def fn(node, lo, hi):
            if not node:
                return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)
        return fn(root, float("-inf"), float("inf"))
        


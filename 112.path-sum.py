#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (37.55%)
# Likes:    935
# Dislikes: 301
# Total Accepted:    314.8K
# Total Submissions: 832.7K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # None 
        if not root: 
            return False
        # leaf node
        if not root.left and not root.right and root.val == sum: 
            return True
        # right or left tree has path sum
        return self.hasPathSum(root.left, sum - root.val) | self.hasPathSum(root.right, sum - root.val)


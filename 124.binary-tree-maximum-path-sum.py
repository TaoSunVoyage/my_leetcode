#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (29.79%)
# Likes:    1565
# Dislikes: 113
# Total Accepted:    192.3K
# Total Submissions: 640.5K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Most-voted solution
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node: 
                return [float('-inf'), float('-inf')]
            rightMax = helper(node.right)
            leftMax  = helper(node.left)
            return [node.val + max(rightMax[0], leftMax[0], 0),
                    max(leftMax + rightMax + [node.val + leftMax[0] + rightMax[0]])]
        return max(helper(root))
    
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0
            rightMax = helper(node.right)
            leftMax = helper(node.left)
            self.max = max(self.max, rightMax + node.val + leftMax)
            return max(node.val + max(leftMax, rightMax), 0)
        self.max = float('-inf')
        _ = helper(root)
        return self.max


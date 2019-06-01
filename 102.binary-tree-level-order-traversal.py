#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (48.06%)
# Likes:    1462
# Dislikes: 38
# Total Accepted:    377.9K
# Total Submissions: 778.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    # My solution
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack = [root]
        res = []
        while stack:
            levelValue = []
            nextLevelNodes = []
            for n in stack:
                levelValue.append(n.val)
                if n.left:
                    nextLevelNodes.append(n.left)
                if n.right:
                    nextLevelNodes.append(n.right)
            res.append(levelValue)
            stack = nextLevelNodes
        return res


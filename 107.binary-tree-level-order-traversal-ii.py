#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (46.41%)
# Likes:    724
# Dislikes: 138
# Total Accepted:    226.3K
# Total Submissions: 483.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
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
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        thisLevel = [root]
        while thisLevel:
            levelValue = []
            nextLevel = []
            for n in thisLevel:
                if n:
                    levelValue.append(n.val)
                    nextLevel += [n.left, n.right]
            if levelValue:
                res.insert(0, levelValue)
            thisLevel = nextLevel
        return res



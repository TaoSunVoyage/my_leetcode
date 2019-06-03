#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (35.16%)
# Likes:    715
# Dislikes: 385
# Total Accepted:    295.9K
# Total Submissions: 838.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # My solution - BFS
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        nodes = [root]
        depth = 1
        while nodes:
            nextNodes = []
            for n in nodes:
                if not n.left and not n.right:
                    return depth
                if n.left: 
                    nextNodes.append(n.left)
                if n.right:
                    nextNodes.append(n.right)
            nodes = nextNodes
            depth += 1
    
    # My solution - recursion
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        if not root.left or not root.right: 
            return 1 + self.minDepth(root.left) + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


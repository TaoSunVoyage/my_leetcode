#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (45.66%)
# Likes:    917
# Dislikes: 68
# Total Accepted:    232K
# Total Submissions: 500.7K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def helper(node, path, res):
            if not node:
                return
            if not node.right and not node.left:
                res.append(path + str(node.val))
            if node.left:
                helper(node.left, path + str(node.val) + '->', res)
            if node.right:
                helper(node.right, path + str(node.val) + '->', res)
        res = []
        helper(root, "", res)
        return res
    
    # Most-voted solution 
    def binaryTreePaths(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res

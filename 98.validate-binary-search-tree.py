#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (25.59%)
# Likes:    1919
# Dislikes: 292
# Total Accepted:    405.6K
# Total Submissions: 1.6M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# Example 1:
# 
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Input: [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
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
    def isValidBST(self, root: TreeNode) -> bool:
        # empty tree
        if not root: 
            return True
        # without children
        if not root.left and not root.right: 
            return True
        # with only right child
        if not root.left:
            if self.isValidBST(root.right):
                node = root.right
                while node.left:
                    node = node.left
                if node.val > root.val:
                    return True
                else:
                    return False
            else:
                return False
        # with only left child
        if not root.right:
            if self.isValidBST(root.left):
                node = root.left
                while node.right:
                    node = node.right
                if node.val < root.val:
                    return True
                else:
                    return False
            else:
                return False
        # with both children
        if self.isValidBST(root.left):
            node = root.left
            while node.right:
                node = node.right
            if node.val >= root.val:
                return False
        else:
            return False
        if self.isValidBST(root.right):
            node = root.right
            while node.left:
                node = node.left
            if node.val <= root.val:
                return False
        else:
            return False
        return True
    
    # Recursion
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if not lower < val < upper:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True
        return helper(root)
    
    # Iteration
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            val = node.val
            if not lower < val < upper:
                return False
            stack.append((node.left, lower, val))
            stack.append((node.right, val, upper))
        return True

    # Inorder traversal
    def isValidBST(self, root: TreeNode) -> bool:
        output = self.inOrder(root)
        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False
        return True
    def inOrder(self, root):
        if not root: return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)


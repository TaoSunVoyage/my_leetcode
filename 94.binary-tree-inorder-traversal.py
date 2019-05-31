#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (56.18%)
# Likes:    1597
# Dislikes: 71
# Total Accepted:    461.6K
# Total Submissions: 814.7K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # My solution - recursive 
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    # My solution - with stack
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        toTraversal = []
        res = []
        node = root
        while True:
            # leaf
            if not node.left and not node.right:
                # add leaf's val
                res.append(node.val)
                # if there are no more nodes, return the result
                if not toTraversal:
                    return res
                else:
                    node = toTraversal.pop()
            # only have right node
            elif not node.left:
                # add current node's value
                res.append(node.val)
                # next is the right node
                node = node.right
            # only have left node
            elif not node.right:
                # put only current node's value into stack
                toTraversal += [TreeNode(node.val)]
                # next is the left node
                node = node.left
            # have both nodes
            else:
                # put right node and current node's value into stack
                toTraversal += [node.right, TreeNode(node.val)]
                # next is the left node
                node = node.left

    # Most-voted solution - with stack
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
    
    # Morris Traversal - without stack
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, current = [], root
        while current:
            if not current.left:
                res.append(current.val)
                current = current.right
            else:
                pre = current.left
                while pre.right:
                    pre = pre.right
                pre.right = current
                temp = current
                current = current.left
                temp.left = None
        return res

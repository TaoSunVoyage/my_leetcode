#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (35.42%)
# Likes:    1216
# Dislikes: 111
# Total Accepted:    138.6K
# Total Submissions: 388.1K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    # # My solution
    # import copy
    # def generateTrees(self, n: int) -> List[TreeNode]:
    #     if n == 0: return []
    #     if n == 1: return [TreeNode(1)]
    #     res = []
    #     # insert into the tree
    #     for root in self.generateTrees(n - 1):
    #         node = root
    #         # how deep the tree is
    #         depth = 0
    #         while node:
    #             depth += 1
    #             node = node.right
    #         # insert at each depth
    #         for i in range(depth + 1):
    #             dummy = TreeNode(None)
    #             dummy.right = copy.deepcopy(root)
    #             cur = dummy
    #             for _ in range(i):
    #                 cur = cur.right
    #             tmp = cur.right
    #             cur.right = TreeNode(n)
    #             cur.right.left = tmp
    #             res.append(dummy.right)
    #     return res

    # Most-voted solution
    def generateTrees(self, n: int) -> List[TreeNode]:
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last + 1)
                    for left in trees(first, root - 1)
                    for right in trees(root + 1, last)] or [None]
        if not n: return []
        return trees(1, n)
    
    # dfs 
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.dfs(1, n + 1)
    
    def dfs(self, start, end):
        if start == end:
            return []
        result = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i+1, end) or [None]:
                    node = TreeNode(i)
                    node.left, node.right  = l, r
                    result.append(node)
        return result

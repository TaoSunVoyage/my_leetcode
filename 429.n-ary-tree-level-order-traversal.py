#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Easy (59.08%)
# Likes:    297
# Dislikes: 34
# Total Accepted:    41K
# Total Submissions: 68K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# We should return its level order traversal:
# 
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
# 
# 
# 
# Note:
# 
# 
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    # My solution
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # if not root:
        #     return []
        level = [root] if root else []
        res = []
        while level:
            values = [node.val for node in level]
            level = [child for node in level for child in node.children]
            # for node in level:
            #     values.append(node.val)
            #     if node.children:
            #         nextlevel += node.children
            # level = nextlevel
            res.append(values)
        return res
            


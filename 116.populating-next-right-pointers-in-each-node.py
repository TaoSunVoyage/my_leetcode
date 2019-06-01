#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (37.54%)
# Likes:    990
# Dislikes: 86
# Total Accepted:    244.5K
# Total Submissions: 645.4K
# Testcase Example:  '{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# 
# Example:
# 
# 
# 
# 
# Input:
# {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
# 
# Output:
# {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
# 
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B.
# 
# 
# 
# 
# Note:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra
# space for this problem.
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    # My solution
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        def helper(l, r):
            if not l: return
            l.next = r
            helper(l.left, l.right)
            helper(l.right, r.left)
            helper(r.left, r.right)
        helper(root.left, root.right)
        return root
    
    # Most-voted solution
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur and cur.left:
            next = cur.left
            while cur:
                cur.left.next = cur.right
                cur.right.next = cur.next and cur.next.left
                cur = cur.next
            cur = next
        return root

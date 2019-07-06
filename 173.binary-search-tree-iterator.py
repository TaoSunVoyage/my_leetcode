#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (48.20%)
# Likes:    1389
# Dislikes: 245
# Total Accepted:    209.2K
# Total Submissions: 426.7K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Note:
# 
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        def toList(root):
            if not root:
                return []
            return toList(root.left) + [root.val] + toList(root.right)
        self.val = toList(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.val.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.val) != 0


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAll(root)
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0
    
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (28.27%)
# Likes:    679
# Dislikes: 58
# Total Accepted:    71.1K
# Total Submissions: 249.1K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i
# to val.
# 
# Example:
# 
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# Note:
# 
# 
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
# 
# 
#

# My solution
class NumArray:
    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            self.left = None
            self.right = None
            self.sumValue = 0
            self.nValue = 0
        elif len(nums) == 1:
            self.left = None
            self.right = None
            self.sumValue = nums[0]
            self.nValue = 1
        else:
            self.left = NumArray(nums[:len(nums)//2])
            self.right = NumArray(nums[len(nums)//2:])
            self.sumValue = self.left.sumValue + self.right.sumValue
            self.nValue = self.left.nValue + self.right.nValue

    def update(self, i: int, val: int) -> None:
        if self.nValue == 1:
            self.sumValue = val
        else:
            if i < self.nValue // 2:
                self.left.update(i, val)
            else:
                self.right.update(i - self.nValue // 2, val)
            self.sumValue = self.left.sumValue + self.right.sumValue
        
    def sumRange(self, i: int, j: int) -> int:
        if j - i + 1 == self.nValue: return self.sumValue
        if i >= self.nValue // 2:
            return self.right.sumRange(i - self.nValue // 2, j - self.nValue // 2)
        if j < self.nValue // 2:
            return self.left.sumRange(i, j)
        return self.left.sumRange(i, self.nValue // 2 - 1) + self.right.sumRange(0, j - self.nValue // 2)


# Most-voted solution
# Standard Segment Tree style
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = 0
    
class NumArray:
    def __init__(self, nums: List[int]):
        def createTree(nums, l, r):
            if l > r:
                return None
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            mid = (l + r) // 2
            root = Node(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)
            root.total = root.left.total + root.right.total
            return root
        self.root = createTree(nums, 0, len(nums) - 1)
    
    def update(self, i: int, val: int) -> None:
        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                return 
            mid = (root.start + root.end) // 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            root.total = root.left.total + root.right.total
        updateVal(self.root, i, val)
    
    def sumRange(self, i: int, j: int) -> int:
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i > mid:
                return rangeSum(root.right, i, j)
            return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)
        return rangeSum(self.root, i, j)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


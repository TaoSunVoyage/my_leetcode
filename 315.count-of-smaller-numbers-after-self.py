#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (37.86%)
# Likes:    1093
# Dislikes: 47
# Total Accepted:    75.8K
# Total Submissions: 199.1K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
# 
# Example:
# 
# 
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
#

class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        hashTable = {v:i for i, v in enumerate(sorted(set(nums)))}
        res = []
        tree = SegmentTree(len(hashTable))
        for i in range(len(nums) - 1, -1, -1):
            res.append(tree.sumRange(0, hashTable[nums[i]] - 1))
            tree.addValue(hashTable[nums[i]], 1)
        return res[::-1]

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sumValue = 0

class SegmentTree:
    # create a tree with n zeros
    def __init__(self, n):
        def createTree(left, right):
            if left > right:
                return None
            if left == right:
                return Node(left, right)
            mid = (left + right) // 2
            root = Node(left, right)
            root.left = createTree(left, mid)
            root.right = createTree(mid + 1, right)
            return root
        self.root = createTree(0, n - 1)
    
    # add val to number at index idx
    def addValue(self, idx, val):
        def addHelper(root, idx, val):
            if idx == root.start == root.end:
                root.sumValue += val
            else:
                mid = (root.start + root.end) // 2
                if idx <= mid:
                    addHelper(root.left, idx, val)
                else:
                    addHelper(root.right, idx, val)
                root.sumValue = root.left.sumValue + root.right.sumValue
        addHelper(self.root, idx, val)

    # sum all numbers from fromIdx to toIdx
    def sumRange(self, fromIdx, toIdx):
        def sumHelper(root, fromIdx, toIdx):
            if fromIdx > toIdx:
                return 0
            if fromIdx == root.start and toIdx == root.end:
                return root.sumValue
            mid = (root.start + root.end) // 2
            if toIdx <= mid:
                return sumHelper(root.left, fromIdx, toIdx)
            elif fromIdx > mid:
                return sumHelper(root.right, fromIdx, toIdx)
            elif fromIdx <= mid < toIdx:
                return sumHelper(root.left, fromIdx, mid) + sumHelper(root.right, mid + 1, toIdx)
        return sumHelper(self.root, fromIdx, toIdx)



# class Solution:
    # # Naive way - O(N^2) Time Limit Exceeded
    # def countSmaller(self, nums: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(nums)):
    #         count = 0
    #         for j in range(i + 1, len(nums)):
    #             if nums[j] < nums[i]:
    #                 count += 1
    #         res.append(count)
    #     return res
    
    # # Time Limit Exceeded
    # def countSmaller(self, nums: List[int]) -> List[int]:
    #     res = []
    #     tree = self.buildTree(nums)
    #     for i in range(len(nums) - 1):
    #         count = self.countByTree(nums[i+1:], nums[i])
    #         res.append(count)
    #     if nums: 
    #         res.append(0)
    #     return res
    
    # def buildTree(self, nums):
    #     def helper(tree, i, left, right):
    #         if left == right:
    #             tree[i] = nums[left]
    #         else:
    #             mid = (left + right) // 2
    #             helper(tree, 2 * i + 1, left, mid)
    #             helper(tree, 2 * i + 2, mid + 1, right)
    #             tree[i] = min(tree[2 * i + 1], tree[2 * i + 2])

    #     tree = [0 for _ in range(len(nums) * 4)]
    #     helper(tree, 0, 0, len(nums)-1)
    #     return tree

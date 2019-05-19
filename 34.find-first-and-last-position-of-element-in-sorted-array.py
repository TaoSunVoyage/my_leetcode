#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (33.39%)
# Likes:    1526
# Dislikes: 85
# Total Accepted:    296.3K
# Total Submissions: 885K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(A, x):
            l, r = 0, len(A) - 1
            while l <= r:
                m = (l + r) // 2
                if A[m] >= x: r = m - 1
                else: l = m + 1
            return l
        
        def binarySearchRight(A, x):
            l, r = 0, len(A) - 1
            while l <= r:
                m = (l + r) // 2
                if A[m] <= x: l = m + 1
                else: r = m - 1 
            return r

        l, r = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return [l, r] if l <= r else [-1, -1]

            



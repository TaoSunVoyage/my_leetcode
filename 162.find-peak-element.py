#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (41.09%)
# Likes:    832
# Dislikes: 1315
# Total Accepted:    240.6K
# Total Submissions: 582.8K
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is greater than its neighbors.
# 
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and
# return its index.
# 
# The array may contain multiple peaks, in that case return the index to any
# one of the peaks is fine.
# 
# You may imagine that nums[-1] = nums[n] = -∞.
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# 
# Example 2:
# 
# 
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak
# element is 2, 
# or index number 5 where the peak element is 6.
# 
# 
# Note:
# 
# Your solution should be in logarithmic complexity.
# 
#
class Solution:
    # My solution - O(N)
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        for i in range(len(nums)):
            if i == 0:
                if nums[i] > nums[i + 1]:
                    return i
            elif i == len(nums) - 1:
                if nums[i-1] < nums[i]:
                    return i
            else:
                if nums[i-1] < nums[i] and nums[i] > nums[i + 1]:
                    return i
    
    # Most voted - O(logN)
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r - 1:
            mid = (l + r) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        
        return l if nums[l] >= nums[r] else r
            


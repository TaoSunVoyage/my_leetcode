#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (57.56%)
# Likes:    812
# Dislikes: 64
# Total Accepted:    60.5K
# Total Submissions: 105.4K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# Given a sorted array consisting of only integers where every element appears
# exactly twice except for one element which appears exactly once. Find this
# single element that appears only once.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# 
# 
# Note: Your solution should run in O(log n) time and O(1) space.
# 
#
class Solution:
    # O(N) solution
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]
            i += 2
    
    # O(logN) solution
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            l_eq = nums[mid - 1] == nums[mid]
            r_eq = nums[mid + 1] == nums[mid]
            if not l_eq and not r_eq:
                return nums[mid]
            elif l_eq and mid % 2 == 1:
                l = mid + 1 
            elif r_eq and mid % 2 == 0:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]

        


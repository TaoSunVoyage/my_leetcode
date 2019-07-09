#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (54.12%)
# Likes:    2123
# Dislikes: 79
# Total Accepted:    485.2K
# Total Submissions: 888.5K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#
class Solution:
    # My solution
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPos = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroPos.append(i)
            else:
                if zeroPos:
                    previous = zeroPos.pop(0)
                    nums[i], nums[previous] = nums[previous], nums[i]
                    zeroPos.append(i)
    
    # Most-voted
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        


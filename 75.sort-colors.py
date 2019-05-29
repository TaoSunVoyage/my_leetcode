#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (41.91%)
# Likes:    1615
# Dislikes: 155
# Total Accepted:    317.7K
# Total Submissions: 753.7K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#
class Solution:
    # My Solution - two passes
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {0:0, 1:0, 2:0}
        for n in nums:
            counter[n] += 1
        zeros, ones, twos = counter[0], counter[1], counter[2]
        for i in range(len(nums)):
            if i < zeros:
                nums[i] = 0
            elif i < zeros + ones:
                nums[i] = 1
            else:
                nums[i] = 2
    
    # My Solution - one pass
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCur = 0
        twoCur = len(nums) - 1
        oneCur = 0
        while oneCur <= twoCur:
            if nums[oneCur] == 0:
                nums[oneCur], nums[zeroCur] = nums[zeroCur], nums[oneCur]
                zeroCur += 1
                oneCur += 1
            elif nums[oneCur] == 1:
                oneCur += 1
            elif nums[oneCur] == 2:
                nums[oneCur], nums[twoCur] = nums[twoCur], nums[oneCur]
                twoCur -= 1
            else:
                raise NotImplementedError()
                
            
        


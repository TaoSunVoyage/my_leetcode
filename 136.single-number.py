#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (59.77%)
# Likes:    2387
# Dislikes: 91
# Total Accepted:    459.2K
# Total Submissions: 764.7K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#
class Solution:
    # My solution - bad thought!
    # each number has its unique bit representation
    # so could just do bit-manipulation

    def singleNumber(self, nums: List[int]) -> int:
        positive, negative = 0, 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                positive ^= 2 ** nums[i]
            else:
                negative ^= 2 ** (-nums[i])
        if positive:
            return len(bin(positive)) - 3
        if negative:
            return 3 - len(bin(negative))
    
    # bit-manipulation 
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
    
    from functools import reduce
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
